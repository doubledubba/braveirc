#!/usr/bin/env python

''' Brave Python IRC client

# Algorithm
1. Authenticate
2. Server goes into engine loop
3. Client queries 'online users'
4. Client queries 'recent chat'
5. Client enters chatterloop
'''

from settings import *

credentials = {'username': 'jnaranjo', 'password': 'test'}



s.connect((HOST, PORT))
# Start connection

auth_token = query('auth', credentials)
send(s, auth_token)

send(s, 'hallo')

# End connection
s.close()
