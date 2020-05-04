import tkinter as tk
import tkinter.messagebox as mb

#from DBMS_Project import *

class AdminGui():
    
    def __init__(self,root,qMessage):
        root.title('Admin')
        self.v = tk.IntVar()
        
        self.rbMaxPlace = tk.Radiobutton(root, value = 1, 
                        text="The historical place with the maximum number of visitors",
                        variable = self.v)
        
        self.rbMaxCity = tk.Radiobutton(root, value = 2, 
                        text="The city with the maximum number of visitors",
                        variable = self.v)
        
        self.rbDetailedCity = tk.Radiobutton(root, value = 3, 
                        text="The number of visitors, the number of male,\n visitors, the number of "
                        "female visitors and the number of local visitors \nand the number of tourists" 
                        "for each city",
                        variable = self.v)
        
        self.rbDetailedPlace = tk.Radiobutton(root, value = 4, 
                        text="The number of visitors, the number of male visitors,\n "
                        "the number of female visitors and the number of local visitors\n"
                        "and the number of tourists for each historical place in a given city ",
                        variable = self.v)
        
        self.radioButton5 = tk.Radiobutton(root, value = 5, 
                        text="The number of visitors, the number of male visitors,\n the number of" 
                        "female visitors and the number of local visitors\n and the number of"
                        "tourists for a given historical place on a given date",
                        variable = self.v)
        
        self.rbMaxPlace.pack()
        self.rbMaxCity.pack()
        self.rbDetailedCity.pack()
        self.rbDetailedPlace.pack()
        self.radioButton5.pack()
    
        tk.Button(root, text='CREATE REPORT',command= self.createQuery).pack()
        print(self.v)

    def createQuery(self):
        selection = self.v.get()
        if(selection == 0): 
            self.root = tk.Tk()
            self.root.withdraw()
            mb.showerror("Error", "Please select one of the options!")
            self.root.destroy()
            return
        messageToServer = "adminQuery" + ";" + str(selection) #QUERY AND QUERY NUMBER message
        print("onclick: ", messageToServer)
        #root.destroy()
