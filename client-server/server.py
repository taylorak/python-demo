"Simple socket server"
import socket

HOST = ""
PORT = 8080


def main():
    "starts socket server"
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(1)

    while True:
        client, _ = server.accept()
        request = client.recv(1024).decode()
        print(request)
        client.send("HTTP/1.0 404 Not Found\r\n".encode())
        client.close()

if __name__ == "__main__":
    main()
