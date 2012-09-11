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
from settings import *

credentials = {'username': 'jnaranjo', 'password': 'test'}

def die(msg=None, exit=0):
    s.close()
    if msg:
        logger.info(msg)
    sys.exit(exit)


s.connect((HOST, PORT))
send = partial(send, s)
recv = partial(recv, s)
rdecode = partial(rdecode, s)
# Start connection

## authenticate
auth_token = query('auth', credentials)
send(auth_token)
auth = rdecode()
auth = auth.get('auth')
if not auth:
    logger.warning('Failed to authenticate!')
    die(exit=1)
else:
    print 'Login successful!'

## get online users
send(query('online users'))
online = rdecode()

print 'Online users:'
pprint(online.get('online'))


# End connection
die()
