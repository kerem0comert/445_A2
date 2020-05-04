import sqlite3
import socket
import threading


class ServerThread(threading.Thread):
    def __init__(self, connection, address):
        self.connection = connection
        self.address = address
        threading.Thread.__init__(self)

    def run(self):
        print(self.address, ": Connection Established!")
        self.connection.send("waiting for auth".encode())
        clientResponse = self.connection.recv(1024).decode()
        if not clientResponse:
            print(self.address, ": Connection Closed!")
            quit()
        print(self.address, ": Client sent auth:", clientResponse) 
        responseArray = clientResponse.split(";") #responseArray = [authHeader, username, password]
        username = responseArray[1]
        password = responseArray[2]
        #here username and password has to be checked in the database
        #authResult will send success or fail accordingly back to client
        #check the roles!
        #if manager login success -> send 2, if admin login success -> send 1
        #  if login fail -> send 0
        authResult = "1".encode() #bad practice to send plain int's without header to client
        self.connection.send(authResult)
        print(self.address, ": auth result sent.")
        clientQueryResponse = clientResponse = self.connection.recv(1024).decode()
        if not clientQueryResponse:
            print(self.address, ": Connection Closed!")
            quit()
        print(self.address, ": clientQueryResponse :", clientQueryResponse)
        queryResult = "QUERY INSERTION SUCCESSS".encode()
        self.connection.send(queryResult)
        print(self.address, ": Finished!")
        quit()

HOST = 'localhost'
PORT = 5000

serverSocket = socket.socket(socket.AF_INET, #for ipv4 communiciation
                        socket.SOCK_STREAM # TCP Protocol
                        )
try:
    serverSocket.bind((HOST,PORT))
except Exception as e:
    print("FATAL ERROR!")
    print("Could not bind port", PORT, "on", HOST, "!")
    print("Maybe socket is being used?")
    print("")
    print("BYE!")
    quit()

#auth -> [header, username, password]
#adminQuery -> [header, selection]
#insertDetails -> [header, totVisitors, maleVisitors, femalVisitors, localVisitors, tourists]
while 1:
    print("Waiting for connection...")
    serverSocket.listen()
    connection, address = serverSocket.accept()
    ServerThread(connection, address).start()



