from tkinter import *
from tkinter import ttk
import tkinter.messagebox as mb

#from DBMS_Project import *

class managerGui():
    
    messageToServer=''
    def __init__(self,root):
        self.root = root
        self.root.title('MANAGER SCREEN')

        Label(text = ' Total Number Of Visitors ',font='Times 15').grid(row=1,column=1,pady=20)
        self.totVisitors = Entry()
        self.totVisitors.grid(row=1,column=2,columnspan=10)

        Label(text = ' The Number Of Male Visitors ',font='Times 15').grid(row=2,column=1,pady=10)
        self.maleVisitors = Entry()
        self.maleVisitors.grid(row=2,column=2,columnspan=10)

        Label(text = ' The Number Of Female Visitors ',font='Times 15').grid(row=3,column=1,pady=10)
        self.femaleVisitors = Entry()
        self.femaleVisitors.grid(row=3,column=2,columnspan=10)

        Label(text = ' The Number Of Local Visitors ',font='Times 15').grid(row=4,column=1,pady=10)
        self.localVisitors = Entry()
        self.localVisitors.grid(row=4,column=2,columnspan=10)

        Label(text = ' The Number Of Tourists ',font='Times 15').grid(row=5,column=1,pady=10)
        self.tourists = Entry()
        self.tourists.grid(row=5,column=2,columnspan=10)

        ttk.Button(text='REPORT',command=self.reportData).grid(row=6,column=2)


    def reportData(self):
        totVisitors = self.totVisitors.get()
        maleVisitors = self.maleVisitors.get() 
        femaleVisitors = self.femaleVisitors.get() 
        localVisitors = self.localVisitors.get() 
        tourists = self.tourists.get() 
        if (not totVisitors or not maleVisitors or not femaleVisitors or not localVisitors or not tourists): mb.showerror("Error", "Everything has to be filled out!")
        else: 
            messageToServer = "rcrd" + ";" + totVisitors + ";" + maleVisitors + ";" + femaleVisitors + ";" + localVisitors + ";" + tourists #record message
            print("onclick: ", messageToServer)
            root.destroy()

if __name__ == '__main__':  # this is to test the gui

    root = Tk()
    root.geometry('450x300')
    application = managerGui(root)

    root.mainloop()