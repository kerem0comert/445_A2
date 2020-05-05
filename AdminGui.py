import tkinter as tk
import tkinter.messagebox as mb

#from DBMS_Project import *

class AdminGui():
    
    def __init__(self,root,qMessage):
        self.root = root
        self.root.title('Admin')
        global v 
        v = tk.IntVar() #first one is seleceted initially
        self.rbValues = {"The historical place with the maximum number of visitors": 1,
                        "The city with the maximum number of visitors": 2,
                        "Extended details for each city" : 3,
                        "Extended details for each historical place in a given city": 4,
                        "Extended details for a historical place by date": 5}

        for (text, value) in self.rbValues.items(): 
            tk.Radiobutton(self.root, text=text, variable=v, 
                        value=value, state=tk.NORMAL).pack(side=tk.TOP, ipady=5)
        self.bGenerateReport = tk.Button(self.root, text='CREATE REPORT',command= self.createQuery).pack()

    def createQuery(self):
        selection = v.get()
        print(selection)
        messageToServer = "adminQuery" + ";" + str(selection) #QUERY AND QUERY NUMBER message
        print("onclick: ", messageToServer)
        #root.destroy()
