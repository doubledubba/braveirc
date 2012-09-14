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
from functools import partial
from pprint import pprint
from multiprocessing import Process

from settings import * # be explicit
import settings

def die(msg=None, exit=0):
    s.close()
    if msg:
        logger.info(msg)
    sys.exit(exit)


def startChat(credentials):
    s.connect((HOST, PORT))
    send = partial(settings.send, s)
    recv = partial(settings.recv, s)
    rdecode = partial(settings.rdecode, s)
    # Start connection

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
