#!/usr/bin/python

import socket

host = socket.gethostname()
port = 8080;

mySocket = socket.socket()
mySocket.bind((host,port))
mySocket.listen()

while True:
    client, addr = mySocket.accept()
    client.send("Hello World".encode())
    client.close()
