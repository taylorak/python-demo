#!/usr/bin/python

import socket

#host = socket.gethostname()
host = ""
port = 8080

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.bind((host,port))
mySocket.listen(1)

print("starting server")
while True:
    client, addr = mySocket.accept()
    #print("request from " + str(addr));
    request = client.recv(1024).decode()
    print(request)
    #reply = "You asked: " + message
    #client.send(reply.encode())
    client.send("HTTP/1.0 404 Not Found\r\n".encode())
    client.close()
