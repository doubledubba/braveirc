#!/usr/bin/env python

import socket

import settings
from settings import HOST, logger

SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SOCKET.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
SOCKET.bind(HOST)
SOCKET.listen(1)

clients = {}

while True:
    sock, sockname = SOCKET.accept()
    print sockname
