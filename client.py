#!/usr/bin/env python

''' Brave Python IRC client

# Algorithm
1. Authenticate
2. Start chatter
'''

from settings import *

USERNAME = 'jnaranjo'
PASSWORD = 'test'


s.connect((HOST, PORT))
# Start connection

auth_token = encode({'auth': {'username': USERNAME, 'password': PASSWORD}})
send(s, auth_token)



# End connection
s.close()
