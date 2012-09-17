#!/usr/bin/env python

import socket
import threading
from functools import partial

import settings
from settings import HOST, logger

SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SOCKET.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
SOCKET.bind(HOST)
SOCKET.listen(1)

clients = []

class Client(threading.Thread):
    def __init__(self, sock, sockname):
        threading.Thread.__init__(self)
        self.name = sockname # override intentional
        self.sock = sock
        clients.append(self)
    
        self.server = settings.Communication(sock)
    def run(self):
        logger.debug('Started connection from: %s' % self.name)
        print self.server.recv()


try:
    while True:
        connection = SOCKET.accept()
        client = Client(*connection)
        client.start()
except KeyboardInterrupt:
    print('Exiting server')

print clients
