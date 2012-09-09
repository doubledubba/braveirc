#!/usr/bin/env python

''' Blank docstring. '''

from settings import *

s.connect((HOST, PORT))

username = 'jnaranjo'

s.sendall(username)  # login
reply = recvall(s, 1028)
print 'The server said', repr(reply)
s.close()
