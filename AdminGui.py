import tkinter as tk
import tkinter.messagebox as mb

#from DBMS_Project import *

class AdminGui():
    
    def __init__(self,root,qMessage):
        root.title('Admin')
        self.v = tk.IntVar(root) #first one is seleceted initially
        self.v.set(1)
        self.rbValues = {"The historical place with the maximum number of visitors": 1,
                        "The city with the maximum number of visitors": 2,
                        "Extended details for each city" : 3,
                        "Extended details for each historical place in a given city": 4,
                        "Extended details for a historical place by date": 5}

        for (text, value) in self.rbValues.items(): 
            tk.Radiobutton(root, text=text, variable=self.v, 
                        value=value).pack(side=tk.TOP, ipady=5)
        self.bGenerateReport = tk.Button(root, text='CREATE REPORT',command= self.createQuery).pack()

    def createQuery(self):
        selection = self.v.get()
        print(selection)
        messageToServer = "adminQuery" + ";" + str(selection) #QUERY AND QUERY NUMBER message
        print("onclick: ", messageToServer)
        #root.destroy()
