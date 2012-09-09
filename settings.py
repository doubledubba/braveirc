import sys
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

arg = lambda i, default: sys.argv[i] if len(sys.argv) > i else default

HOST = arg(1, '127.0.0.1')
PORT = arg(2, 1060)


def recvall(sock, length):
    data = ''
    while len(data) < length:
        more = sock.recv(length - len(data))
        if not more:
            raise RuntimeError('socket closed %d bytes into a %d-byte message'
                    % (len(data), length))
        data += more
    return data

if __name__ == '__main__':
    print 'Host:', HOST
    print 'Port:', PORT
