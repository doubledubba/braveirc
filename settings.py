import sys
import socket
import json
import logging

import easygui as eg

logging.basicConfig(format='[%(levelname)s] [%(asctime)s]: %(message)s',
        level=logging.DEBUG)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

arg = lambda i, default: sys.argv[i] if len(sys.argv) > i else default

HOST = arg(1, '127.0.0.1')
PORT = arg(2, 1060)

DEBUG = True
DEBUG = False

logger = logging.getLogger()

def recvall(sock, length):
    data = ''
    while len(data) < length:
        more = sock.recv(length - len(data))
        if not more:
            raise RuntimeError('socket closed %d bytes into a %d-byte message'
                    % (len(data), length))
        data += more
    return data


def send(sc, msg):
    '''Sends a message to the server after sending a length header'''
    length = str(len(msg)).zfill(4)
    if len(length) > 4:
        raise ValueError('The message can\'t be longer than 9999 bytes!')

    sc.sendall(length)
    sc.sendall(msg)


def recv(sc):
    msg_length = recvall(sc, 4)
    if not msg_length.isalnum():
        print msg_length
        raise ValueError('Invalid message length header!')
    msg_length = int(msg_length)

    return recvall(sc, msg_length)


def query(method, *dicts):
    request = {method if dicts else 'command': {} if dicts else method}
    for dictionary in dicts:
        for key in dictionary:
            request[method][key] = dictionary[key]

    return encode(request)


def decode(string):
    '''Parses a JSON string into a python object.'''

    try:
        return json.loads(string)
    except:
        logger.warning('Error occurred while trying to decode: %s' % string)


def encode(object):
    '''Encodes a python object into a JSON string.'''
    try:
        return json.dumps(object)
    except ValueError, tb:
        logger.critical(str(tb))


def rdecode(sc, get=None):
    response = recv(sc)
    response = decode(response)
    if get:
        response = response.get(get)
    return response


def dictencode(**kwargs):
    raw = dict(**kwargs)
    return encode(raw)


def getCredentials():
    '''Query user for username and password. Return as a dict

    Future: Add secure password caching
    '''

    msg = "Enter logon information"
    title = "Brave IRC Network"
    fieldNames = ['Username', 'Password']
    fieldValues = []  # we start with blanks for the values
    fieldValues = eg.multpasswordbox(msg, title, fieldNames)

    # make sure that none of the fields was left blank
    while 1:
        if fieldValues == None: break
        errmsg = ""
        for i in range(len(fieldNames)):
            if fieldValues[i].strip() == "":
                errmsg = errmsg + ('"%s" is a required field.\n\n' % fieldNames[i])
        if errmsg == "": 
            break # no problems found
        else:
            # show the box again, with the errmsg as the message
            fieldValues = eg.multpasswordbox(errmsg, title, fieldNames, fieldValues)

    if DEBUG:
        fieldValues = 'jnaranjo', 'test'

    credentials = {'username': fieldValues[0], 'password': fieldValues[1]}

    return credentials


if __name__ == '__main__':
    print 'Host:', HOST
    print 'Port:', PORT
