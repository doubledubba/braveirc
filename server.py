#!/usr/bin/env python

''' Blank docstring. '''

from settings import *


s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(1)
while True:
    print 'Listening at', s.getsockname()
    sc, sockname = s.accept()
    print 'We have accepted a connection from', sockname
    print 'Socket connects', sc.getsockname(), 'and', sc.getpeername()
    message = recvall(sc, 16)
    print 'The incoming sixteen-octet message says', repr(message)
    sc.sendall('Farewell, client')
    sc.close()
    print 'Reply sent, socket closed'
