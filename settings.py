import sys
import socket
import json
import logging

logging.basicConfig(format='[%(levelname)s] [%(asctime)s]: %(message)s',
        level=logging.DEBUG)
logger = logging.getLogger()

arg = lambda i, default: sys.argv[i] if len(sys.argv) > i else default
HOSTNAME = arg(1, '127.0.0.1')
PORT = int(arg(2, 1060))
HOST = (HOSTNAME, PORT)


class Communication(object):
    def __init__(self, socket, name=None):
        self.socket = socket
        self.username = name

    def send_raw(self, msg):
        '''Sends a message to the server after sending a length header'''
        length = str(len(msg)).zfill(4)
        if len(length) > 4:
            raise ValueError('The message can\'t be longer than 9999 bytes!')

        self.socket.sendall(length)
        self.socket.sendall(msg)

    def recvall(self, length):
        data = ''
        while len(data) < length:
            remaining = length - len(data)
            more = self.socket.recv(remaining)
            if not more:
                raise RuntimeError('socket closed %d bytes into a %d-byte message'
                        % (len(data), length))
            data += more
        return data

    def recv_raw(self):
        '''Receives a message of arbitrary length.'''
        msg_length = self.recvall(4)
        if not msg_length.isdigit():
            raise ValueError('Invalid message length header (%r)!' % msg_length)
        msg_length = int(msg_length)

        return self.recvall(msg_length)

    def send(self, obj): # Encode object in JSON then send it
        if obj is not None:
            obj = json.dumps(obj)
            self.send_raw(obj)
        else:
            print 'send method did not get an object to send!'

    def recv(self): # Receive JSON message and decode it
        response = self.recv_raw()
        return json.loads(response)

    def get(self, key):
        response = self.recv()
        return response.get(key)


