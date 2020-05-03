import tkinter as tk
import tkinter.messagebox as mb

#from DBMS_Project import *

class LoginGui():
    def __init__(self, root, qMessage):
        self.qMessage = qMessage #the message queue to talk to the network thread

        self.labelUsername = tk.Label(root, text="Username: ").grid(row=0,column=0)
        self.labelPassword = tk.Label(root, text= "Password: ").grid(row=1,column=0)
        self.entryUsername = tk.Entry(root, width=20)

        #the grid decleration for the entries has to be divided into multiple lines
        #see https://stackoverflow.com/a/1102053/11330757
        self.entryUsername.grid(row=0,column=1)
        self.entryPassword = tk.Entry(root, show="*", width=20)
        self.entryPassword.grid(row=1,column=1)

        self.buttonLogin = tk.Button(root, text="Login", bg="blue", fg="white", state='disabled', command = self.onLoginClick)
        self.buttonLogin.grid(row=2,column=1)
        self.labelConnection = tk.Label(root, text="Trying to connect to the server...")
        self.labelConnection.grid(row=3,column=1)
        


    def onLoginClick(self):
        username = self.entryUsername.get()
        password = self.entryPassword.get() 
        if not username: mb.showerror("Error", "Username cannot be empty!")
        if not password: mb.showerror("Error", "Password cannot be empty!")
        else:
            self.buttonLogin.config(state="disabled")
            messageToServer = "auth" + ";" + username + ";" + password
            print("onclick: ", messageToServer)
            if not self.qMessage.full(): self.qMessage.put(messageToServer) #send the login data to network thread
