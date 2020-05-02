from tkinter import *
from tkinter import ttk

#from DBMS_Project import *

class adminGui():
    
    messageToServer=''
    selection=0
    def __init__(self,root):
        self.root = root
        self.root.title('ADMIN SCREEN')
        v = IntVar()
        
        radioButton1 = Radiobutton(root, value = 1, text="The historical place with the maximum number of visitors",command= v.set(1))
        radioButton2 = Radiobutton(root, value = 2, text="The city with the maximum number of visitors",command= v.set(2))
        radioButton3 = Radiobutton(root, value = 3, text="The number of visitors, the number of male,\n visitors, the number of female visitors and the number of local visitors \nand the number of tourists for each city",command= v.set(3))
        radioButton4 = Radiobutton(root, value = 4, text="The number of visitors, the number of male visitors,\n the number of female visitors and the number of local visitors\n and the number of tourists for each historical place in a given city ",command= v.set(4))
        radioButton5 = Radiobutton(root, value = 5, text="The number of visitors, the number of male visitors,\n the number of female visitors and the number of local visitors\n and the number of tourists for a given historical place on a given date",command= v.set(5))
        radioButton1.pack()
        radioButton2.pack()
        radioButton3.pack()
        radioButton4.pack()
        radioButton5.pack()
        self.selection = v.get()
        ttk.Button(text='CREATE REPORT',command= self.createQuery).pack()


    def createQuery(self):
        value = self.selection
        messageToServer = "qry" + ";" + str(value) #QUERY AND QUERY NUMBER message
        print("onclick: ", messageToServer)
        root.destroy()

if __name__ == '__main__':  # this is to test the gui

    root = Tk()
    root.geometry('500x300')
    application = adminGui(root)

    root.mainloop()