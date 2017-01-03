import socket

mySocket = socket.socket()
host = socket.gethostname()
port = 8080

mySocket.connect((host, port))
print(mySocket.recv(1024).decode())
mySocket.close
