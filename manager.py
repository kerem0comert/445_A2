import tkinter as tk
import tkinter.messagebox as mb #messagebox doesn't get imported implicitly by the above import 




root = tk.Tk()   #initialize the tkinter window
root.title("---MANAGER LOGIN---")
root.geometry("300x300")

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
    mb.showinfo("Information","Informative message")

buttonLogin = tk.Button(root, text="Login",bg="blue",fg="white", 
                            command = onLoginClick).grid(row=2,column=1)




root.mainloop() #this should be called after all the inits


