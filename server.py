#!/usr/bin/env python

''' Blank docstring. '''

import threading
import os
import hashlib
import sqlite3
from functools import partial
from settings import *

DB = os.path.join(os.path.dirname(__file__), 'db')
DB = os.path.join(DB, 'braveirc.db')
DB = os.path.abspath(DB)
if not os.path.isfile(DB):
    open(DB, 'a')

digest = lambda password: hashlib.md5(password).hexdigest()

conn = sqlite3.connect(DB, check_same_thread=False)
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, '
        'username VARCHAR(255), password VARCHAR(255))')

conn.commit()

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(HOST)
s.listen(1)


class Client(threading.Thread):
    def __init__(self, sc, sockname):
        self.sc = sc
        self.sockname = sockname
        self.username = ''
        self.send = partial(send, sc)
        self.recv = partial(recv, sc)
        self.rdecode = partial(rdecode, sc)
        self.close = self.sc.close
        threading.Thread.__init__(self)

    def login(self):
        token = decode(self.recv())
        auth = token.get('auth')
        if not auth or not isinstance(token, dict): return
        username = auth.get('username')
        password = auth.get('password')
        if not username or not password: return

        spassword = cur.execute('select password from users where username = ?',
                (username,)).fetchone()
        if not spassword: return
        spassword = spassword[0]

        self.authenticated = True if spassword == digest(password) else False
        if self.authenticated:
            logger.info('Authenticated: %s' % username)
            self.username = username
            return True

    def execute(self, command):
        logger.debug('Issuing the "%s" command.' % command)

        if command == 'online users':
            online = [client.username for client in clients if
                    client.is_alive()]
            response = dictencode(online=online)
            self.send(response)


    def run(self):
        logger.debug('Started connection from: %s' %  str(self.sockname))

        if not self.login():
            logger.warning('Failed auth from %s' % str(self.sockname))
            response = dictencode(auth=False)
            self.send(response)
            return
        else:
            response = encode(dict(auth=True))
            self.send(response)

        while True:
            try:
                request = self.rdecode()
                logger.debug('Request: %s' % request)
                if isinstance(request, dict):
                    command = request.get('command')
                    if command:
                        self.execute(command)

            except RuntimeError, tb:
                logger.debug('Shutting down socket!')
                break


        self.close()

clients = []


def mainLoop():
    while True:
        connection = s.accept()
        client = Client(*connection)
        client.start()
        client.name = connection[1]
        clients.append(client)


def addUser(username, password):
    password = digest(password)
    cur.execute('insert into users (username, password) values (?, ?)',
            (username, password))
    conn.commit()


def showUsers():
    for row in cur.execute('select * from users'):
        print row

if __name__ == '__main__':
    try:
        mainLoop()
    except KeyboardInterrupt:
        print 'Clients:', clients


