import sys
import socket
import json
import logging

logging.basicConfig(format='[%(levelname)s] [%(asctime)s]: %(message)s',
        level=logging.DEBUG)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

arg = lambda i, default: sys.argv[i] if len(sys.argv) > i else default

HOSTNAME = arg(1, '127.0.0.1')
PORT = arg(2, 1060)

HOST = (HOSTNAME, PORT)

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


if __name__ == '__main__':
    print 'Host:', HOST
    print 'Port:', PORT
