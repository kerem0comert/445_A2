import tkinter as tk
import tkinter.messagebox as mb
from tkinter import ttk
from time import sleep
import re

#from DBMS_Project import *

class AdminGui():
    
    def __init__(self, root, qMessage, cities, hp, username):
        self.root = root
        self.qMessage = qMessage
        self.cities = cities
        self.places = hp
        self.username = username
        root.title('Admin')
        self.v = tk.IntVar(root) #first one is selected initially
        self.v.set(1)
        self.selectedCity = tk.StringVar(root, value = "Please select")
        self.selectedPlace = tk.StringVar(root, value = "Please select")
        self.date = "00/00/0000"
        self.dateRegex = '^[0-9]{4}-[0-9]{2}-[0-9]{2}$'

        self.welcomeTitle= tk.Label(root, text="Welcome " + self.username + "!").pack()

        self.rbValues = {"The historical place with the maximum number of visitors": 1,
                        "The city with the maximum number of visitors": 2,
                        "Extended details for each city" : 3,
                        "Extended details for each historical place in a given city": 4,
                        "Extended details for a historical place by date": 5}

        for (text, value) in self.rbValues.items(): 
            tk.Radiobutton(root, text=text, variable=self.v, 
                        value=value, command = self.printExtra).pack(side=tk.TOP, ipady=5)
        self.bGenerateReport = tk.Button(root, text='CREATE REPORT',command= self.createQuery)
        self.bGenerateReport.pack()
        self.extendedForThird = tk.Label(root, text = "The number of visitors, the number of male visitors, the number of female visitors" + 
        "\nand the number of local visitors and the number of tourists for each city  ",font='Times 10')
        self.extendedForFourth = tk.Label(root, text = "The number of visitors, the number of male visitors, the number of female visitors \nand the number of local visitors and the number of tourists for each historical place in a given city",font='Times 10')
        self.extendedForFifth = tk.Label(root, text = "The number of visitors, the number of male visitors, the number of female visitors \nand the number of local visitors and the number of tourists for a given historical place on a given date",font='Times 10')
        
        self.dropdownTitleCity= tk.Label(root, text="Choose a City")
        self.dropdownForFifthCity = ttk.Combobox(root, values=list(self.cities.keys()), textvariable=self.selectedCity, state="readonly", width=25)
        self.dropdownForFifthCity.bind('<<ComboboxSelected>>', self.updateBox)
        self.dropdownTitlePlace= tk.Label(root, text="Choose a Place")
        self.dropdownForFifthPlace = ttk.Combobox(root, textvariable=self.selectedPlace, state="disabled", width=25)
        self.dropdownForFifthPlace.bind('<<ComboboxSelected>>', self.packDate)
        
        self.dateTitle= tk.Label(root, text="Enter Date (yyyy-mm-dd):")
        self.dateEntry = tk.Entry(root)

    def updateBox(self, eventObject):
        self.dropdownForFifthPlace["values"] = list(self.places.get(self.cities.get(self.dropdownForFifthCity.get())).keys())
        self.dropdownForFifthPlace["state"] = "readonly"

    def packDate(self,*args):
        self.dateTitle.pack(side=tk.TOP, ipady=5)
        self.dateEntry.pack(side=tk.TOP, ipady=5)

    def printExtra(self):
        selection = self.v.get()
        if (selection == 3):
            self.extendedForFourth.pack_forget()
            self.extendedForFifth.pack_forget()
            self.dropdownTitlePlace.pack_forget()
            self.dropdownForFifthPlace.pack_forget()
            self.dropdownTitleCity.pack_forget()
            self.dropdownForFifthCity.pack_forget()
            self.dateTitle.pack_forget()
            self.dateEntry.pack_forget()
            self.extendedForThird.pack(side=tk.TOP, ipady=5)
            self.dateTitle.pack(side=tk.TOP, ipady=5)
            self.dateEntry.pack(side=tk.TOP, ipady=5)
        elif (selection == 4):
            self.extendedForThird.pack_forget()
            self.extendedForFifth.pack_forget()
            self.dropdownForFifthCity.pack_forget()
            self.dropdownTitleCity.pack_forget()
            self.dropdownForFifthPlace.pack_forget()
            self.dropdownTitlePlace.pack_forget()
            self.dateTitle.pack_forget()
            self.dateEntry.pack_forget()
            self.extendedForFourth.pack(side=tk.TOP, ipady=5)
            self.dateTitle.pack(side=tk.TOP, ipady=5)
            self.dateEntry.pack(side=tk.TOP, ipady=5)
        elif (selection == 5):
            self.extendedForFourth.pack_forget()
            self.extendedForThird.pack_forget()
            self.dateTitle.pack_forget()
            self.dateEntry.pack_forget()
            self.extendedForFifth.pack(side=tk.TOP, ipady=5)
            self.dropdownTitleCity.pack(side=tk.TOP, ipady=5)
            self.dropdownForFifthCity.pack(side=tk.TOP, ipady=5)
            self.dropdownTitlePlace.pack(side=tk.TOP, ipady=5)
            self.dropdownForFifthPlace.pack(side=tk.TOP, ipady=5)
        else:
            self.extendedForThird.pack_forget()
            self.extendedForFourth.pack_forget()
            self.extendedForFifth.pack_forget()
            self.dropdownForFifthCity.pack_forget()
            self.dropdownTitleCity.pack_forget()
            self.dropdownForFifthPlace.pack_forget()
            self.dropdownTitlePlace.pack_forget()
            self.dateTitle.pack_forget()
            self.dateEntry.pack_forget()

    def createQuery(self):
        
        selection = self.v.get()
        if(selection == 5):
            self.checkDateRegex()
            messageToServer = "adminQuery" + ";" + str(selection) + ";" + self.selectedPlace.get() + ";" + self.dateEntry.get()
        if(selection == 3 or selection == 4):
            self.checkDateRegex()
            messageToServer = "adminQuery" + ";" + str(selection) + ";" + self.dateEntry.get()
        else:
            messageToServer = "adminQuery" + ";" + str(selection) #QUERY AND QUERY NUMBER message
        print("onclick: ", messageToServer)
        self.qMessage.put(self.bGenerateReport)
        self.qMessage.put(selection)
        self.qMessage.put(messageToServer)
        self.root = tk.Tk()
        self.root.withdraw()
        self.bGenerateReport.config(state="disabled")
       
    def checkDateRegex(self):
        if not re.match(self.dateRegex, self.dateEntry.get()):
                self.root = tk.Tk()
                self.root.withdraw()
                mb.showerror("Date Error", "Date is not of yyyy-mm-dd format!")
                self.root.destroy()
                self.bGenerateReport.config(state="normal")
                return


    @staticmethod
    def displayMessage(selection, serverQueryResponse):
        # create another Tk root just for preventing create second empty window when info mb displayed
        root = tk.Tk()
        root.withdraw()
        if (selection == 5):
            if(serverQueryResponse[0]!=0):
                message = ""
                message += serverQueryResponse[0] + "\n" + "V=" + serverQueryResponse[1] +" M=" + serverQueryResponse[2] + " F=" + serverQueryResponse[3] + " L=" + serverQueryResponse[4] + " T=" + serverQueryResponse[5] + "\n"
                mb.showinfo(title="Query Result", message=message)
            else:
                mb.showerror(title="Error",message= "Query Result Is Empty!")
        elif (selection == 3 or selection == 4):
            if(serverQueryResponse[0]!="None"):
                message = ""
                if(selection==3):
                    for x in serverQueryResponse:
                        message += serverQueryResponse[0] + "\n" + "V=" + serverQueryResponse[1] +" M=" + serverQueryResponse[2] + " F=" + serverQueryResponse[3] + " L=" + serverQueryResponse[4] + " T=" + serverQueryResponse[5] + "\n"
                    message += "V=The Number Of Visitors\nM=The Number Of Male Visitors\nF=The Number Of Female Visitors\nL=The Number Of Local Visitors\nT=The Number Of Tourists"
                    mb.showinfo(title="Query Result", message=message)
                else:
                    message += serverQueryResponse[0] + "\n" + "V=" + serverQueryResponse[1] +" M=" + serverQueryResponse[2] + " F=" + serverQueryResponse[3] + " L=" + serverQueryResponse[4] + " T=" + serverQueryResponse[5] + "\n"
                    mb.showinfo(title="Query Result", message=message)
            else:
                mb.showerror(title="Error",message= "Query Result Is Empty!")
        elif (selection == 2):
            if(serverQueryResponse!="None"):
                mb.showinfo(title="Query Result",message= "City with the most number of visitors is "+serverQueryResponse)
            else:
                mb.showerror(title="Error",message= "Query Result Is Empty!")
        else:
            if(serverQueryResponse!="None"):
                mb.showinfo(title="Query Result", message="Historical place with the most number of visitors is "+serverQueryResponse)
            else:
                mb.showerror(title="Error",message= "Query Result Is Empty!")