#!/usr/bin/env python

import socket
from threading import Thread
from functools import partial
from datetime import datetime

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
            try:
                txt = self.recv()['msg']
            except RuntimeError:
                logger.debug('RuntimeError!')
                if self in clients:
                    clients.remove(self)
                self.shutdown()
                break

            line = '%s: %s' % (txt['username'], txt['body'])
            logger.info(line)
            msg = txt['body']
            logger.debug('Clients: %d' % len(clients))
            for client in clients:
                if not client.isAlive():
                    clients.remove(client)
                    continue
                client.update(msg, txt['username'])

    def login(self):
        self.username, password = self.get('credentials')
        if not self.username or not password:
            self.shutdown()
            return

        self.authenticated = verifyUser(self.username, password) # Bool
        if self.authenticated:
            logger.info('Logged in: %s' % self.username)
            self.send(True)
            return True
        else:
            logger.info('Auth failed: %s' % self.username)
            self.send(False)

    def update(self, msg, username):
        text = {'msg': {'body': msg, 'user': username, 'time':
            datetime.now().strftime('%I:%M %P')}}
        self.send(text)


    def shutdown(self):
        logger.info('Logged off: %s' % self.username)
        self.socket.close()


def main():
    try:
        while True:
            connection = SOCKET.accept()
            client = Client(*connection)
            client.start()
    except KeyboardInterrupt:
        print('Exiting server')

if __name__ == '__main__':
    main()

print clients
