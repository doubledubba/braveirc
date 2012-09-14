#!/usr/bin/env python

''' Brave Python IRC client

# Algorithm
1. Authenticate
2. Server goes into engine loop
3. Client queries 'online users'
4. Client queries 'recent chat'
5. Client enters chatterloop
'''

import sys
import socket
from functools import partial
from pprint import pprint
from multiprocessing import Process

import settings
from settings import HOST, logger
from settings import query, send, recv, rdecode


makeSocket = lambda: socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def exit_(s, msg=None, exit=0):
    s.close()
    if msg:
        logger.info(msg)
    sys.exit(exit)


def authentic(credentials):
    s = makeSocket()
    s.connect(HOST)
    
    # Convenience functions
    send = partial(settings.send, s) # send(string)
    recv = partial(settings.recv, s) # recv() -> Encoded string
    rdecode = partial(settings.rdecode, s) # recv() -> Decoded string
    die = partial(exit_, s) # exit cleanly

    auth_token = query('auth', credentials)
    send(auth_token)
    auth = rdecode(get='auth')
    if not auth:
        err = 'Failed to authenticate!'
        logger.warning(err)
        die(exit=1)
        authenticated = False
    else:
        logger.info('Login successful!')
        authenticated = True

    s.close()
    return authenticated




def startChat(credentials): # deprecated -> salvage and reconstruct
    s = makeSocket()

    # Convenience functions
    send = partial(settings.send, s) # send(string)
    recv = partial(settings.recv, s) # recv() -> Encoded string
    rdecode = partial(settings.rdecode, s) # recv() -> Decoded string
    die = partial(exit_, s) # exit cleanly
    # Start connection
    s.connect((HOST, PORT))

    ## authenticate
    auth_token = query('auth', credentials)
    send(auth_token)
    auth = rdecode(get='auth')
    if not auth:
        err = 'Failed to authenticate!'
        logger.warning(err)
        die(exit=1)
    else:
        logger.info('Login successful!')

    ## get online users
    send(query('online users'))
    online = rdecode()

    print 'Online users:'
    pprint(online.get('online'))


    # get recent chat

    # start chatter

    # End connection
    die()


