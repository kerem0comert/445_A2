import tkinter as tk
import tkinter.messagebox as mb

#from DBMS_Project import *

class ManagerGui():
    def __init__(self, root, qMessage, hpManagerID, hpCode, hpName, hpCityName, username):
        root.title('Manager')
        self.qMessage = qMessage
        self.hpManagerID = hpManagerID
        self.hpCode = hpCode
        self.hpName = hpName
        self.username = username
        self.hpCityName = hpCityName

        rowCounter = 1

        tk.Label(root, text = "Welcome back " + self.username + "!",font='Times 15').grid(row=rowCounter,column=1,pady=10)
        rowCounter += 1

        tk.Label(root, text = "Historical Place: " + self.hpName,font='Times 15').grid(row=rowCounter,column=1,pady=10)
        rowCounter += 1

        tk.Label(root, text = "City: " + self.hpCityName,font='Times 15').grid(row=rowCounter,column=1,pady=10)
        rowCounter += 1

        tk.Label(root, text = ' Total Number Of Visitors: ',font='Times 15').grid(row=rowCounter,column=1,pady=20)
        self.entryTotVisitors = tk.Entry(root)
        self.entryTotVisitors.grid(row=rowCounter,column=2,columnspan=10)
        rowCounter += 1

        tk.Label(root, text = ' The Number Of Male Visitors: ',font='Times 15').grid(row=rowCounter,column=1,pady=10)
        self.entryMaleVisitors = tk.Entry(root)
        self.entryMaleVisitors.grid(row=rowCounter,column=2,columnspan=10)
        rowCounter += 1

        tk.Label(root, text = ' The Number Of Female Visitors: ',font='Times 15').grid(row=rowCounter,column=1,pady=10)
        self.entryFemaleVisitors = tk.Entry(root)
        self.entryFemaleVisitors.grid(row=rowCounter,column=2,columnspan=10)
        rowCounter += 1

        tk.Label(root, text = ' The Number Of Local Visitors: ',font='Times 15').grid(row=rowCounter,column=1,pady=10)
        self.entryLocalVisitors = tk.Entry(root)
        self.entryLocalVisitors.grid(row=rowCounter,column=2,columnspan=10)
        rowCounter += 1

        tk.Label(root, text = ' The Number Of Tourists: ',font='Times 15').grid(row=rowCounter,column=1,pady=10)
        self.entryTourists = tk.Entry(root)
        self.entryTourists.grid(row=rowCounter,column=2,columnspan=10)
        rowCounter += 1

        tk.Button(root, text='REPORT',command=self.reportData).grid(row=rowCounter,column=2)


    def reportData(self):
        try:
            #inputs must be integers, if not integers then gives error
            totVisitors = int(self.entryTotVisitors.get())
            maleVisitors = int(self.entryMaleVisitors.get()) 
            femaleVisitors = int(self.entryFemaleVisitors.get()) 
            localVisitors = int(self.entryLocalVisitors.get()) 
            tourists = int(self.entryTourists.get()) 
            #totalvisitorsmust be equal to other visitors summed up
            if ((totVisitors != maleVisitors + femaleVisitors) or (totVisitors != localVisitors + tourists)):
                self.root = tk.Tk()
                self.root.withdraw()
                mb.showerror("Error", "Total Visitor must be equal to other fields summed up!")
                self.root.destroy()
            #every value has to be positive
            elif (totVisitors<0 or maleVisitors<0 or femaleVisitors<0 or localVisitors<0 or tourists<0):
                self.root = tk.Tk()
                self.root.withdraw()
                mb.showerror("Error", "No field can be NEGATIVE!")
                self.root.destroy()
            #if no error then send message to server
            else:
                messageToServer = "insertDetails" + ";" + str(totVisitors) + ";" + str(maleVisitors) + ";" + str(femaleVisitors) + ";" + str(localVisitors) + ";" + str(tourists) + ";" + self.hpCode #record message
                print("onclick: ", messageToServer)
                self.qMessage.put(messageToServer)
        except ValueError:
            try:
                #check float error
                totVisitors = float(self.entryTotVisitors.get())
                maleVisitors = float(self.entryMaleVisitors.get())
                femaleVisitors = float(self.entryFemaleVisitors.get())
                localVisitors = float(self.entryLocalVisitors.get())
                tourists = float(self.entryTourists.get())
                self.root = tk.Tk()
                self.root.withdraw()
                mb.showerror("Error", "Please Do NOT Enter Floats!, Integers Only!")
                self.root.destroy()
            except ValueError:
                #check string error
                totVisitors = self.entryTotVisitors.get()
                maleVisitors = self.entryMaleVisitors.get()
                femaleVisitors = self.entryFemaleVisitors.get()
                localVisitors = self.entryLocalVisitors.get()
                tourists = self.entryTourists.get()
                #check empty field error, if any of the fields is empty give error
                if (not str(totVisitors) or not str(maleVisitors) or not str(femaleVisitors) or 
                not str(localVisitors) or not str(tourists)):             
                # create another Tk root just for preventing create second empty window when info mb displayed
                    self.root = tk.Tk()
                    self.root.withdraw()
                    mb.showerror("Error", "Everything has to be filled out!")
                    self.root.destroy()
                #if no fields are empty give inputted a string error
                else:
                    self.root = tk.Tk()
                    self.root.withdraw()
                    mb.showerror("Error", "You Entered A String!, Integers ONLY!")
                    self.root.destroy()
            

