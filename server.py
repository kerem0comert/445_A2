import sqlite3
import socket
import threading


class ServerThread(threading.Thread):
    def __init__(self, connection, address):
        self.connection = connection
        self.address = address
        threading.Thread.__init__(self)
       

    def run(self): 
        clientResponse = ""
        while "auth" not in clientResponse: #no login data is received yet
            message = "waiting for auth".encode()
            self.connection.send(message)
            clientResponse = self.connection.recv(1024).decode()
        print("Client sent auth:", clientResponse) 
        responseArray = clientResponse.split(";") #responseArray = [authHeader, username, password]
        username = responseArray[1]
        password = responseArray[2]
        #here username and password has to be checked in the database
        #authResult will send success or fail accordingly back to client
        #check the roles!
        #if manager login success -> send 2, if admin login success -> send 1
        #  if login fail -> send 0
        authResult = "2".encode() #bad practice to send plain int's without header to client
        self.connection.send(authResult)
        print("auth result sent.")
        clientQueryResponse = clientResponse = self.connection.recv(1024).decode()
        print(clientQueryResponse)
        queryResult = "QUERY INSERTION SUCCESSS".encode()
        self.connection.send(queryResult)
        


HOST = 'localhost'
PORT = 5000


serverSocket = socket.socket(socket.AF_INET, #for ipv4 communiciation
                        socket.SOCK_STREAM # TCP Protocol
                        )

serverSocket.bind((HOST,PORT))



#auth -> [header, username, password]
#adminQuery -> [header, selection]
#insertDetails -> [header, totVisitors, maleVisitors, femalVisitors, localVisitors, tourists]
while 1:
    print("Waiting for connection...")
    serverSocket.listen()
    connection, address = serverSocket.accept()
    ServerThread(connection, address).start()



