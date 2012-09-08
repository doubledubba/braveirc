# Brave IRC

A simple IRC network implemented in python using TCP sockets

Under development by Luis Naranjo <luisnaranjo733@gmail.com>

## Development algorithm

+ Client makes connection to server
+ Server asks for authentication credentials
+ Client provides credentials (username and password)
+ Server verifies credentials in a secure manner
+ Server welcomes the user or gives error message and shuts down connection

+ If client is welcomed:
    + Server will provide a list of online and offline users
    + Show last 5 lines of chat
    + Start chat session with everyone that is connected

## Design decisions

+ Both the server and client scripts will use the TCP implementation in the
  python standard library
+ The server will be blocking, and it will dispatch threads to handle the
  client socket connections

## Pending design decisions

+ Object Relational Mapper
    + Django
    + SQLAlchemy
    + Python standard lib sqlite3 module
+ Database backend
    + SQLITE
    + MySQL
    + Postgres
+ Web UI for registering users?
    + Django
    + Flask
    + Pyramid
