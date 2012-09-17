#!/usr/bin/env python

import socket
from threading import Thread
from functools import partial

from settings import HOST, logger, Communicate

SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SOCKET.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
SOCKET.bind(HOST)
SOCKET.listen(1)

clients = []

class Client(Thread, Communicate):
    def __init__(self, sock, sockname):
        Thread.__init__(self)
        Communicate.__init__(self, sock)
        clients.append(self)

    def run(self):
        logger.debug('Started connection from: %s' % self.name)


try:
    while True:
        connection = SOCKET.accept()
        client = Client(*connection)
        client.start()
except KeyboardInterrupt:
    print('Exiting server')

print clients
