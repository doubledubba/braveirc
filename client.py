#!/usr/bin/env python

''' Brave Python IRC client

# Algorithm
1. Authenticate
2. Server goes into engine loop
3. Client queries 'online users'
4. Client queries 'recent chat'
5. Client enters chatterloop
'''

from functools import partial
from settings import *

credentials = {'username': 'jnaranjo', 'password': 'test'}



s.connect((HOST, PORT))
send = partial(send, s)
recv = partial(recv, s)
# Start connection

## authenticate
auth_token = query('auths', credentials)
send(auth_token)
authenticated = recv()
if authenticated:
    print authenticated




# End connection
s.close()
