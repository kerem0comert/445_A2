import tkinter as tk
import tkinter.messagebox as mb

#from DBMS_Project import *

class AdminGui():
    
    def __init__(self,root,qMessage):
        root.title('Admin')
        self.v = tk.IntVar(root) #first one is seleceted initially
        self.v.set(1)
        self.defaultCity = tk.StringVar(root)
        self.defaultPlace = tk.StringVar(root)
        self.date = "00/00/0000"
        self.rbValues = {"The historical place with the maximum number of visitors": 1,
                        "The city with the maximum number of visitors": 2,
                        "Extended details for each city" : 3,
                        "Extended details for each historical place in a given city": 4,
                        "Extended details for a historical place by date": 5}

        for (text, value) in self.rbValues.items(): 
            tk.Radiobutton(root, text=text, variable=self.v, 
                        value=value, command = self.printExtra).pack(side=tk.TOP, ipady=5)
        self.bGenerateReport = tk.Button(root, text='CREATE REPORT',command= self.createQuery).pack()
        self.extendedForThird = tk.Label(root, text = "The number of visitors, the number of male visitors, the number of female visitors" + 
        "\nand the number of local visitors and the number of tourists for each city  ",font='Times 10')
        self.extendedForFourth = tk.Label(root, text = "The number of visitors, the number of male visitors, the number of female visitors \nand the number of local visitors and the number of tourists for each historical place in a given city",font='Times 10')
        self.extendedForFifth = tk.Label(root, text = "The number of visitors, the number of male visitors, the number of female visitors \nand the number of local visitors and the number of tourists for a given historical place on a given date",font='Times 10')
        

        # Dictionary with options
        self.cities = { 'Mardin','Hakkari','Gaziantep','Boston','SoykaninEvi'}
        self.places = ['one','two','three']
        self.defaultCity.set('City:') # set the default option
        self.dropdownForFifthCity = tk.OptionMenu(root, self.defaultCity, *self.cities)
        self.dropdownTitleCity= tk.Label(root, text="Choose a City")
        self.defaultPlace.set('Place:') # set the default option
        self.dropdownForFifthPlace = tk.OptionMenu(root, self.defaultPlace, *self.places)
        self.dropdownTitlePlace= tk.Label(root, text="Choose a Place")
        self.dateTitle= tk.Label(root, text="Enter Date:")
        self.dateEntry = tk.Entry(root)
        self.defaultCity.trace("w",self.loadPlaces)
        self.defaultPlace.trace("w",self.inputDate)
    def printExtra(self):
        selection = self.v.get()
        if (selection == 3):
            self.extendedForFourth.pack_forget()
            self.extendedForFifth.pack_forget()
            self.dropdownTitlePlace.pack_forget()
            self.dropdownForFifthPlace.pack_forget()
            self.dropdownTitleCity.pack_forget()
            self.dropdownForFifthCity.pack_forget()
            self.extendedForThird.pack(side=tk.TOP, ipady=5)
        elif (selection == 4):
            self.extendedForThird.pack_forget()
            self.extendedForFifth.pack_forget()
            self.dropdownForFifthCity.pack_forget()
            self.dropdownTitleCity.pack_forget()
            self.dropdownForFifthPlace.pack_forget()
            self.dropdownTitlePlace.pack_forget()
            self.extendedForFourth.pack(side=tk.TOP, ipady=5)
        elif (selection == 5):
            self.extendedForFourth.pack_forget()
            self.extendedForThird.pack_forget()
            self.extendedForFifth.pack(side=tk.TOP, ipady=5)
            self.dropdownTitlePlace.pack(side=tk.TOP, ipady=5)
            self.dropdownForFifthCity.pack(side=tk.TOP, ipady=5)
            
    def inputDate(self,*args):
        self.dateTitle.pack(side=tk.TOP, ipady=5)
        self.dateEntry.pack(side=tk.TOP, ipady=5)
        self.date = self.dateEntry.get()

    def loadPlaces(self,*args):
        #take palces from the database
        #update places list with according places list
        self.places = ['test','test2']  #you need to get the values from the database
        menu = self.dropdownForFifthPlace["menu"]
        menu.delete(0, "end")
        #this for updates the values in the old list with the values from the new list
        for string in self.places:
            menu.add_command(label=string,command=lambda value=string: self.defaultPlace.set(value))
        print(self.places)
        
        self.dropdownTitlePlace.pack(side=tk.TOP, ipady=5)
        self.dropdownForFifthPlace.pack(side=tk.TOP, ipady=5)
        
    def createQuery(self):
        selection = self.v.get()
        if(selection == 5):
            messageToServer = "adminQuery" + ";" + str(selection) + ";" + self.defaultPlace.get() + ";" + self.date
            print("onclick: ", messageToServer)
        else:
            print(selection)
            messageToServer = "adminQuery" + ";" + str(selection) #QUERY AND QUERY NUMBER message
            print("onclick: ", messageToServer)
            #root.destroy()
