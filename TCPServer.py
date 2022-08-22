#!/usr/bin/python3

import socket

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 444

serverSocket.bind((host, port))

serverSocket.listen(3)

while True:
    clientSocket, address = serverSocket.accept()

    print("receive connection from" % str(address))

    message = "Hello! thank you for connecting to the server" * "\r\n"

    clientSocket.send(message.encode('ascii'))

    clientSocket.close()