#!/usr/bin/env python

''' Blank docstring. '''

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
while True:
    sc, sockname = s.accept()
    token = recv(sc)
    sc.close()

    token = decode(token) or token
    user = login(token)
    if user:
        print '%s has succesfully logged in.' % user
    else:
        print 'Unidentified user login failed.'
