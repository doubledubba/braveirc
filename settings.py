import sys
import socket
import json
import logging

logging.basicConfig(format='[%(levelname)s] [%(asctime)s]: %(message)s',
        level=logging.DEBUG)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

arg = lambda i, default: sys.argv[i] if len(sys.argv) > i else default

HOST = arg(1, '127.0.0.1')
PORT = arg(2, 1060)

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


def send(s, msg):
    '''Sends a message to the server after sending a length header'''
    length = str(len(msg)).zfill(4)
    if len(length) > 4:
        raise ValueError('The message can\'t be longer than 9999 bytes!')

    s.send(length)
    s.sendall(msg)


def recv(sc):
    msg_length = sc.recv(4)
    if not msg_length.isalnum():
        raise ValueError('Invalid message length header!')
    msg_length = int(msg_length)
    msg = sc.recv(msg_length)
    return msg

if __name__ == '__main__':
    print 'Host:', HOST
    print 'Port:', PORT
