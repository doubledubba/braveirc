#!/usr/bin/env python

import socket
from threading import Thread
from functools import partial

from settings import HOST, logger, Communication
from db import verifyUser

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
        if not self.login():
            self.shutdown()
            return
        while True:
            txt = self.recv()['msg']
            print '%s: %s' % (txt['username'], txt['body'])
            msg = txt['body']
            for client in clients:
                if not client.isAlive():
                    clients.remove(client)
                    continue
                client.update(msg, txt['username'])

    def login(self):
        self.username, password = self.get('credentials')
        print 'Logged in:', self.username
        if not self.username or not password:
            self.shutdown()
            return

        self.authenticated = verifyUser(self.username, password) # Bool
        if self.authenticated:
            self.send(True)
            return True
        else:
            self.send(False)

    def update(self, msg, username):
        text = {'msg': {'body': msg, 'user': username}}
        print 'Updating:', username
        self.send(text)


    def shutdown(self):
        logger.debug('Manually shutting down socket')
        self.socket.close()

try:
    while True:
        connection = SOCKET.accept()
        client = Client(*connection)
        client.start()
except KeyboardInterrupt:
    print('Exiting server')

print clients
