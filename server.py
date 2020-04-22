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
    
    message = "SERVER >>> Connection successful".encode()
    connection.send(message)

    clientResponse = connection.recv(1024).decode()
    while clientResponse != "CLIENT >>> TERMINATE":
        print(clientResponse)
        message = input("SERVER >>> ")
        message = ("SERVER >>> " + message).encode()
        connection.send(message)
        clientResponse = connection.recv(1024).decode()
    message = "SERVER >>> Successfully terminated".encode()
    connection.send(message)
    connection.close()
    print("Connection terminated successfully.")