"simple socket client"
import socket

HOST = socket.gethostname()
PORT = 8080


def connect():
    "connects to socket server"
    client = socket.socket()
    client.connect((HOST, PORT))
    client.send("Hello".encode())
    print(client.recv(1024).decode())
    client.close()

if __name__ == "__main__":
    connect()
