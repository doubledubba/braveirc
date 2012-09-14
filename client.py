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
from settings import HOST, PORT, logger
from settings import query


def exit_(s, msg=None, exit=0):
    s.close()
    if msg:
        logger.info(msg)
    sys.exit(exit)



def startChat(credentials):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Convenience functions
    send = partial(settings.send, s)
    recv = partial(settings.recv, s)
    rdecode = partial(settings.rdecode, s)
    die = partial(exit_, s)
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


