import tkinter as tk
import tkinter.messagebox as mb #messagebox doesn't get imported implicitly by the above import
import socket
import threading
import os
import queue #used to pass the username-password data to ClientNetworkThread
from time import sleep
from LoginGui import *
from ManagerGui import *
from AdminGui import *

qMessage = queue.Queue(5)
MANAGER_SUCCESS = "success"
ADMIN_SUCCESS = "admin"
MANAGER_GUI_READY = "managerGuiReady"
MANAGER_QUERY_SUCCESS = "QUERY INSERTION SUCCESSS"
MANAGER_QUERY_FAIL = "QUERY INSERTION FAILED"

class ClientNetworkThread(threading.Thread):
    def __init__(self, root):
        self.root = root
        threading.Thread.__init__(self)
        print("ClientNetworkThread initialized.")
    def run(self):
        HOST = 'localhost'
        PORT = 5000
        print("Attempting connection...")
        global mySocket
        mySocket = socket.socket(socket.AF_INET, #for ipv4 communiciation
                                socket.SOCK_STREAM # TCP Protocol
                                )
        try:
            mySocket.connect((HOST,PORT))
            print("Connected to server.")
            managerLoginGui.labelConnection.config(text='Connected to server')
            managerLoginGui.buttonLogin.config(state="normal")
            serverResponse = mySocket.recv(1024).decode()
            print(serverResponse)
            if serverResponse == "waiting for auth": #server is waiting for login data
                while qMessage.empty(): sleep(1)
                if not qMessage.empty(): #login data came from the gui
                    guiResponse = qMessage.get()
                    guiResponseList = guiResponse.split(";")
                    global username
                    username = guiResponseList[1]
                    messageToServer = guiResponse.encode()
                    try: 
                        mySocket.send(messageToServer)
                        # serverLoginResponse -> staffID;authResponse;roleID;hpCode;hpName;hpCityName
                        serverLoginResponse = mySocket.recv(1024).decode().split(";")
                        serverAuthResponse = serverLoginResponse[1]
                        print("Server auth response: ", serverAuthResponse)
                        if int(serverAuthResponse) == 0: 
                            mb.showerror("Error", "Login failed")
                            end_app()
                        elif int(serverAuthResponse) == 2:
                            mb.showinfo("Login", "Logged in successfully!")
                            qMessage.put(MANAGER_SUCCESS)
                            qMessage.put(serverLoginResponse[0]) # staffID
                            qMessage.put(serverLoginResponse[2]) # hpCode
                            qMessage.put(serverLoginResponse[3]) # hpName
                            qMessage.put(serverLoginResponse[4]) # hpCityName
                            self.root.destroy()
                            sleep(2) #wait until gui thread can take the queue message
                            while qMessage.empty(): sleep(1)
                            queryToServer = qMessage.get().encode()
                            mySocket.send(queryToServer)
                            serverQueryResponse = mySocket.recv(1024).decode()
                            # create another Tk root just for preventing create second empty window when info mb displayed
                            self.root = tk.Tk()
                            self.root.withdraw()
                            if serverQueryResponse == MANAGER_QUERY_SUCCESS:
                                mb.showinfo("Success", "Insertion successful")
                            else:
                                mb.showerror("Error", "You cant send statistics more than once in a day")
                            self.root.destroy()
                            # kill proccess here, we dont have anything to do left
                            end_app()
                        elif int(serverAuthResponse) == 1:
                            mb.showinfo("Login", "Logged in successfully!")
                            qMessage.put(ADMIN_SUCCESS)
                            qMessage.put(serverLoginResponse[0]) # staffID
                            self.root.destroy()
                            sleep(2) #wait until gui thread can take the queue message
                            while qMessage.empty(): sleep(1)
                            queryToServer = qMessage.get().encode()
                            mySocket.send(queryToServer)
                            serverQueryResponse = mySocket.recv(1024).decode()
                            # ADD QUERY SELECTIONS HERE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                            end_app()
                    except: pass
        except: 
            mb.showerror("Error", "Connection to server failed or closed.")
            end_app()

def end_app():
    try:
        mySocket.close()
    except: pass
    os._exit(0)
    
if __name__ == '__main__':
    loginRoot = tk.Tk()
    loginRoot.geometry('250x130')
    loginRoot.protocol("WM_DELETE_WINDOW", end_app)
    loginRoot.resizable(False, False)
    print("Main Thread:", threading.get_ident())
    managerLoginGui = LoginGui(loginRoot, qMessage)
    networkThread = ClientNetworkThread(loginRoot)
    networkThread.start()
    loginRoot.mainloop()
    print("out of mainloop")
    while qMessage.empty(): sleep(0.5)
    loginStatus = qMessage.get()
    staffID = qMessage.get()
    print("status in ui thread", loginStatus)
    if(loginStatus == MANAGER_SUCCESS):
        hpCode = qMessage.get()
        hpName = qMessage.get()
        hpCityName = qMessage.get()
        managerGuiRoot = tk.Tk()
        managerGuiRoot.geometry('450x450')
        managerGuiRoot.protocol("WM_DELETE_WINDOW", end_app)
        managerGuiRoot.resizable(False, False)
        print("Main Thread:", threading.get_ident())
        managerGui = ManagerGui(managerGuiRoot, qMessage, staffID, hpCode, hpName, hpCityName, username)
        managerGuiRoot.mainloop()
    elif(loginStatus == ADMIN_SUCCESS): 
        AdminGuiRoot = tk.Tk()
        AdminGuiRoot.geometry('450x300')
        AdminGuiRoot.protocol("WM_DELETE_WINDOW", end_app)
        AdminGuiRoot.resizable(False, False)
        print("Main Thread:", threading.get_ident())
        adminGui = AdminGui(AdminGuiRoot, qMessage)
        AdminGuiRoot.mainloop()
