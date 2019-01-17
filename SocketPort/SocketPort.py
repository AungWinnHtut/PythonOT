import socket

try:
    socket.gethostbyaddr('192.168.0.101')
except socket.herror:
    print('Unknown host')


