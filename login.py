from tkinter import *
from tkinter import ttk
import tkinter.messagebox as mb

#from DBMS_Project import *

class loginGui():
    messageToServer=''
    def __init__(self,root):
        self.root = root
        self.root.title('LOGIN SCREEN')

        Label(text = ' Username ',font='Times 15').grid(row=1,column=1,pady=20)
        self.username = Entry()
        self.username.grid(row=1,column=2,columnspan=10)

        Label(text = ' Password ',font='Times 15').grid(row=2,column=1,pady=10)
        self.password = Entry(show='*')
        self.password.grid(row=2,column=2,columnspan=10)

        ttk.Button(text='LOGIN',command=self.loginUser).grid(row=3,column=2)


    def loginUser(self):
        username = self.username.get()
        password = self.password.get() 
        if not username: mb.showerror("Error", "Username cannot be empty!")
        if not password: mb.showerror("Error", "Password cannot be empty!")
        else: 
            messageToServer = "auth" + ";" + username + ";" + password
            print("onclick: ", messageToServer)
            destroy()
            #if not qMessage.full(): qMessage.put(messageToServer) #send the login data to network thread
    
if __name__ == '__main__':

    root = Tk()
    root.geometry('425x225')
    application = loginGui(root)

    root.mainloop()