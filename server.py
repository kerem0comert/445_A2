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
    clientResponse = ""
    while "auth" not in clientResponse: #no login data is received yet
        message = "waiting for auth".encode()
        connection.send(message)
        clientResponse = connection.recv(1024).decode()
    print("Client sent auth:", clientResponse) 
    responseArray = clientResponse.split(";") #responseArray = [authHeader, username, password]
    username = responseArray[1]
    password = responseArray[2]
    #here username and password has to be checked in the database
    #authResult will send success or fail accordingly back to client
    authResult = "1".encode() #bad practice to send plain int's without header to client
    connection.send(authResult)
    print("auth result sent.")
