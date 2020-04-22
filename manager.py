import tkinter as tk
import tkinter.messagebox as mb #messagebox doesn't get imported implicitly by the above import 
import socket



def initNetwork():
    HOST = 'localhost'
    PORT = 5000

    print("Attempting connection...")
    mySocket = socket.socket(socket.AF_INET, #for ipv4 communiciation
                            socket.SOCK_STREAM # TCP Protocol
                            )

    try: mySocket.connect((HOST,PORT))
    except: mb.showerror("Error", "Couldn't connect to the server.")
    print("Connected to server.")
    serverResponse = mySocket.recv(1024).decode()
    while serverResponse != "SERVER >>> TERMINATE":
        print(serverResponse)
        message = input("CLIENT >>> ")
        message = ("CLIENT >>> " + message).encode()
        mySocket.send(message)
        serverResponse = mySocket.recv(1024).decode()
    
    message = "CLIENT >>> TERMINATE".encode()
    mySocket.send()
    print("Connection terminated")
    mySocket.close()

#------------GUI

root = tk.Tk()   #initialize the tkinter window
root.title("Manager Login")
root.geometry("250x80")
root.eval('tk::PlaceWindow %s center' % root.winfo_pathname(
                root.winfo_id())) #center the window when created


labelUsername = tk.Label(root, text="Username: ").grid(row=0,column=0)
labelPassword = tk.Label(root, text= "Password: ").grid(row=1,column=0)
entryUsername = tk.Entry(root, width=20)

#the grid decleration for the entries has to be divided into multiple lines
#see https://stackoverflow.com/a/1102053/11330757
entryUsername.grid(row=0,column=1)
entryPassword = tk.Entry(root, width=20)
entryPassword.grid(row=1,column=1)


def onLoginClick():
    username = entryUsername.get()
    password = entryPassword.get() 
    if not username: mb.showerror("Error", "Username cannot be empty!")
    if not password: mb.showerror("Error", "Password cannot be empty!")
    else: 
        mb.showinfo("Information","Informative message")

buttonLogin = tk.Button(root,text="Login",bg="blue",fg="white", 
                            command = onLoginClick).grid(row=2,column=1)

initNetwork()
root.mainloop() #this should be called after all the inits



