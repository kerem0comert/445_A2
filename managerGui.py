import tkinter as tk
import tkinter.messagebox as mb

#from DBMS_Project import *

class ManagerGui():
    
    messageToServer=''
    def __init__(self,root, qMessage):
        root.title('MANAGER SCREEN')
        self.qMessage = qMessage
        tk.Label(root, text = ' Total Number Of Visitors ',font='Times 15').grid(row=1,column=1,pady=20)
        self.entryTotVisitors = tk.Entry(root)
        self.entryTotVisitors.grid(row=1,column=2,columnspan=10)

        tk.Label(root, text = ' The Number Of Male Visitors ',font='Times 15').grid(row=2,column=1,pady=10)
        self.entryMaleVisitors = tk.Entry(root)
        self.entryMaleVisitors.grid(row=2,column=2,columnspan=10)

        tk.Label(root, text = ' The Number Of Female Visitors ',font='Times 15').grid(row=3,column=1,pady=10)
        self.entryFemaleVisitors = tk.Entry(root)
        self.entryFemaleVisitors.grid(row=3,column=2,columnspan=10)

        tk.Label(root, text = ' The Number Of Local Visitors ',font='Times 15').grid(row=4,column=1,pady=10)
        self.entryLocalVisitors = tk.Entry(root)
        self.entryLocalVisitors.grid(row=4,column=2,columnspan=10)

        tk.Label(root, text = ' The Number Of Tourists ',font='Times 15').grid(row=5,column=1,pady=10)
        self.entryTourists = tk.Entry(root)
        self.entryTourists.grid(row=5,column=2,columnspan=10)

        tk.Button(root, text='REPORT',command=self.reportData).grid(row=6,column=2)


    def reportData(self):
        totVisitors = self.entryTotVisitors.get()
        maleVisitors = self.entryMaleVisitors.get() 
        femaleVisitors = self.entryFemaleVisitors.get() 
        localVisitors = self.entryLocalVisitors.get() 
        tourists = self.entryTourists.get() 
        if (not totVisitors or not maleVisitors or not femaleVisitors or 
            not localVisitors or not tourists): 
            mb.showerror("Error", "Everything has to be filled out!")
        else: 
            messageToServer = "insertDetails" + ";" + totVisitors + ";" + maleVisitors + ";" + femaleVisitors + ";" + localVisitors + ";" + tourists #record message
            print("onclick: ", messageToServer)
            self.qMessage.put(messageToServer)

