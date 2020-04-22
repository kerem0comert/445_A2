import sqlite3
import socket

HOST = 'localhost'
PORT = 5000


serverSocket = socket.socket(socket.AF_INET, #for ipv4 communiciation
                        socket.SOCK_STREAM # TCP Protocol
                        )

serverSocket.bind((HOST,PORT))

while 1:
    print("Waiting for connection...")
    serverSocket.listen()
    connection, address = serverSocket.accept()
    print("Connection is recieved from, ", address[0])
    clientResponse = "hey client"
    while "auth" not in clientResponse: #no login data is received yet
        message = "waiting for auth".encode()
        connection.send(message)
        print(clientResponse)
        clientResponse = connection.recv(1024).decode()
    print("Client sent auth: ", clientResponse)
    authResult = "You authed bro".encode()
    connection.send(authResult)