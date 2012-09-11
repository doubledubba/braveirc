#!/usr/bin/env python

''' Blank docstring. '''

import threading
from functools import partial
from settings import *


def login(token):
    '''Authenticates user credentials.

    Returns username if authenticated succesfully.'''

    if not token: return
    if 'auth' not in token: return

    token = token['auth'] # nested dictionary - only one we need

    if 'username' not in token or 'password' not in token: return

    return token['username']


s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(1)



class Client(threading.Thread):
    def __init__(self, sc, sockname):
        self.sc = sc
        self.sockname = sockname
        self.username = ''
        self.send = partial(send, sc)
        self.recv = partial(recv, sc)
        self.close = self.sc.close
        threading.Thread.__init__(self)

    def login(self):
        token = decode(self.recv())
        auth = token.get('auth')
        if not auth or not isinstance(token, dict): return
        username = auth.get('username')
        password = auth.get('password')
        if not username or not password: return

        self.authenticated = True
        if self.authenticated:
            logger.info('Authenticated: %s' % username)
            self.username = username
            return True

    def execute(self, command):
        logger.debug('Issuing the "%s" command.' % command)
        if command == 'logged in':
            if self.authenticated:
                self.send('Yes')
            else:
                self.send('No')


    def run(self):
        logger.debug('Started connection from: %s' %  str(self.sockname))

        if not self.login():
            logger.warning('Failed auth from %s' % str(self.sockname))
            self.send('') # so the recv on the other side doesn't hang
            return
        else:
            self.send('yes')

        while True:
            try:
                request = self.recv()
                request = decode(request)
                logger.debug('Request: %s' % request)
                if isinstance(request, dict):
                    command = request.get('command')
                    if command:
                        self.execute(command)

            except RuntimeError, tb:
                logger.debug('Shutting down socket!')
                break


        self.close()

clients = []


def mainLoop():
    while True:
        connection = s.accept()
        client = Client(*connection)
        client.start()
        client.name = connection[1]
        clients.append(client)

try:
    mainLoop()
except KeyboardInterrupt:
    print 'Clients:', clients


