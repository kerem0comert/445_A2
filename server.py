import sqlite3
import socket
import threading
from time import sleep
from Database import *

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
        loginResult = DB.login(username, password)
        self.connection.send((str(loginResult[0]) + ";" + str(loginResult[1])).encode())
        sleep(0.5) # just in case
        if loginResult[1] == 2:
            self.connection.send((str(DB.getHpCode(loginResult[0])) + ";" + DB.getHpName(DB.getHpCode(loginResult[0])) + ";" + DB.getHpCityName(loginResult[0])).encode())
        elif loginResult[1] == 1:
            pass
        print(self.address, ": login result sent.")
        clientResponse = self.connection.recv(1024).decode()
        if not clientResponse:
            print(self.address, ": Connection Closed!")
            quit()
        print(self.address, ": clientResponse :", clientResponse)
        clientQueryResponse = clientResponse.split(";")
        if clientQueryResponse[0] == "insertDetails":
            del clientQueryResponse[0]
            # clientQueryResponse -> [totVisitors, maleVisitors, femaleVisitors, localVisitors, tourists, hpCode]
            if DB.sendStatistics(clientQueryResponse):
                queryResult = "QUERY INSERTION FAILED".encode()
            else:
                queryResult = "QUERY INSERTION SUCCESSS".encode()
            self.connection.send(queryResult)
        print(self.address, ": Finished!")

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

DB = Database()

print("Listening on", serverSocket.getsockname())
#auth -> [header, username, password]
#adminQuery -> [header, selection]
#insertDetails -> [header, totVisitors, maleVisitors, femalVisitors,
#localVisitors, tourists]
while 1:
    serverSocket.listen()
    connection, address = serverSocket.accept()
    ServerThread(connection, address).start()



