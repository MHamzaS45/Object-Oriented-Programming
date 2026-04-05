# DropDown menu

from tkinter import *

root = Tk()
root.title("DropDown Menu")
root.geometry("720x480")

options=[" Option 1", 
         "Option 2",
           "Option 3", 
           "Option 4", 
           "Option 5"
]

selectItem = StringVar()
selectItem.set(options[0])

def show ():
    myLabel=Label(root, text=selectItem.get()).pack()

drop = OptionMenu(root, selectItem, *options)
drop.pack()

myButton = Button(root, text = "Show Selection", command=show).pack()

root.mainloop()

