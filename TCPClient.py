#!/usr/bin/python3

import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostbyname()
port = 444

clientSocket.connect((host, port))

message = clientSocket.recv(1024)

clientSocket.close()

print(message.decode('ascii'))
