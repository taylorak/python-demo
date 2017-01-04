"import socket library"
import socket

HOST = ""
PORT = 8080

SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER.bind((HOST, PORT))
SERVER.listen(1)

while True:
    CLIENT, ADDR = SERVER.accept()
    #print("request from " + str(addr));
    REQUEST = CLIENT.recv(1024).decode()
    print(REQUEST)
    #reply = "You asked: " + message
    #client.send(reply.encode())
    CLIENT.send("HTTP/1.0 404 Not Found\r\n".encode())
    CLIENT.close()
