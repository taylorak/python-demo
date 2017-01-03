#!/usr/bin/python

import socket

host = socket.gethostname()
port = 8080;

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.bind((host,port))
mySocket.listen()


while True:
    client, addr = mySocket.accept()
    message = client.recv(1024).decode();
    reply = "You asked: " + message
    client.sendall(reply.encode())
    client.close()
