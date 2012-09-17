#!/usr/bin/env python

import socket
from threading import Thread
from functools import partial

from settings import HOST, logger, Communication

SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SOCKET.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
SOCKET.bind(HOST)
SOCKET.listen(1)

clients = []

class Client(Thread, Communication):
    def __init__(self, sock, sockname):
        Thread.__init__(self)
        Communication.__init__(self, sock)
        self.name = sockname
        clients.append(self)

    def run(self):
        logger.debug('Started connection from: %s' % self.name)

        credentials = self.recv()
        self.username = credentials.get('username')
        if not self.username:
            self.shutdown()
            return

        print self.username, 'logged in'


    def shutdown(self):
        logger.debug('Shutting down socket')
        self.socket.close()

try:
    while True:
        connection = SOCKET.accept()
        client = Client(*connection)
        client.start()
except KeyboardInterrupt:
    print('Exiting server')

print clients
