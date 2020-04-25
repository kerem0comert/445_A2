import tkinter as tk
import tkinter.messagebox as mb #messagebox doesn't get imported implicitly by the above import 
import socket
import threading
import queue #used to pass the username-password data to ClientNetworkThread
from time import sleep

qMessage = queue.Queue(1) #only the login data is there for the networkThread to consume,
                          #so queue capacity = 1


class ClientNetworkThread(threading.Thread):
    def __init__(self, root, lblConnection):
        threading.Thread.__init__(self)
        print("ClientNetworkThread initialized.")
        self.lblConnection = lblConnection
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
            self.lblConnection.config(text="Connection to server is successful!", fg="green")
            serverResponse = mySocket.recv(1024).decode()
            print(serverResponse)
            while serverResponse == "waiting for auth": #server is waiting for login data 
                while qMessage.empty(): sleep(1)
                if not qMessage.empty(): #login data came from the gui
                    messageToServer = qMessage.get().encode()
                    try: mySocket.send(messageToServer)
                    except Exception as e: print(e)
                    serverAuthResponse = mySocket.recv(1024).decode()
                    print("Server auth response: ", serverAuthResponse)
                    if int(serverAuthResponse) == 1: 
                        mb.showinfo("Login", "Logged in successfully!")
                        
        except: 
            mb.showerror("Error", "Connection to server failed or closed.")
            self.lblConnection.config(text="Connection to server failed.\n"
                                   "Restart the program to try again.", fg="red")


    
    

#------------GUI

root = tk.Tk()   #initialize the tkinter window
root.title("Manager Login")
root.geometry("250x130")
#root.eval('tk::PlaceWindow %s center' % root.winfo_pathname(
                #root.winfo_id())) #center the window when created


labelUsername = tk.Label(root, text="Username: ").grid(row=0,column=0)
labelPassword = tk.Label(root, text= "Password: ").grid(row=1,column=0)
entryUsername = tk.Entry(root, width=20)

#the grid decleration for the entries has to be divided into multiple lines
#see https://stackoverflow.com/a/1102053/11330757
entryUsername.grid(row=0,column=1)
entryPassword = tk.Entry(root,  show="*", width=20)
entryPassword.grid(row=1,column=1)


def onLoginClick():
    username = entryUsername.get()
    password = entryPassword.get() 
    if not username: mb.showerror("Error", "Username cannot be empty!")
    if not password: mb.showerror("Error", "Password cannot be empty!")
    else: 
        messageToServer = "auth" + ";" + username + ";" + password
        print("onclick: ", messageToServer)
        if not qMessage.full(): qMessage.put(messageToServer) #send the login data to network thread
        root.update()


buttonLogin = tk.Button(root,text="Login",bg="blue",fg="white", 
                            command = onLoginClick)
buttonLogin.grid(row=2,column=1)
labelConnection = tk.Label(root, text="Trying to connect to the server...")
labelConnection.grid(row=3,column=1)

clientNetworkThread = ClientNetworkThread(root, labelConnection)
clientNetworkThread.start()

root.mainloop() #this should be called after all the inits



