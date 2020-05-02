import tkinter as tk
import tkinter.messagebox as mb #messagebox doesn't get imported implicitly by the above import 
import socket
import threading
import queue #used to pass the username-password data to ClientNetworkThread
from time import sleep
from LoginGui import *


qMessage = queue.Queue(1) #only the login data is there for the networkThread to consume,
                          #so queue capacity = 1


class ClientNetworkThread(threading.Thread):
    def __init__(self, root):
        threading.Thread.__init__(self)
        print("ClientNetworkThread initialized.")
        #self.lblConnection = lblConnection
    def run(self):
        HOST = 'localhost'
        PORT = 5000
        print("Attempting connection...")
        mySocket = socket.socket(socket.AF_INET, #for ipv4 communiciation
                                socket.SOCK_STREAM # TCP Protocol
                                )
        try: 
            mySocket.connect((HOST,PORT))
            print("Connected to server.")
            #self.lblConnection.config(text="Connection to server is successful!", fg="green")
            serverResponse = mySocket.recv(1024).decode()
            print(serverResponse)
            while serverResponse == "waiting for auth": #server is waiting for login data 
                while qMessage.empty(): sleep(1)
                if not qMessage.empty(): #login data came from the gui
                    messageToServer = qMessage.get().encode()
                    try: 
                        mySocket.send(messageToServer)
                    except Exception as e: print(e)
                    serverAuthResponse = mySocket.recv(1024).decode()
                    print("Server auth response: ", serverAuthResponse)
                    if int(serverAuthResponse) == 1: 
                        mb.showinfo("Login", "Logged in successfully!")
                        
        except: 
            mb.showerror("Error", "Connection to server failed or closed.")
            """self.lblConnection.config(text="Connection to server failed.\n"
                                   "Restart the program to try again.", fg="red")"""


    
if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('250x130')
    #root.eval('tk::PlaceWindow %s center' % root.winfo_pathname(
    #   root.winfo_id())) #center the window when created
    managerLoginGui = LoginGui(root, qMessage)
    networkThread = ClientNetworkThread(root)
    networkThread.start()
    root.mainloop()

