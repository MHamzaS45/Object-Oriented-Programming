# Import UI file

from tkinter import *
from tkinter import messagebox

print("App starting...")
# TK() = new window

root = Tk()

root.title("Messagebox-practice")
root.title("DropDownbox")
root.geometry("400x400")
root.title("RadioButtons")

#Radio button selections

SelectOption = [
    ("selection1", "Hyndai"), 
    ("selection2", "BMW"), 
    ("selection3", "Volvo"),
    ("selection4", "Ford")
]

choices = StringVar()

choices.set("selection1")


#Option 

options = [
    "First",
    "Second",
    "Third",
    "Fourth",
    "Fifth"
]


selectItem = StringVar()
selectItem.set(options[0])


#Function button pressing button handler

def ICLicked(): 
    #   Write text label which
    buttonClickLabel = Label(root, text="Button pressed") 
    buttonClickLabel.pack()



# Message box popup
def popup(): 
     response = messagebox.askyesno("Messagebox wants to say: ", "Here I am")
     if response == 1: 
         Label (root, text="You clicked Yes Button").pack()
     else: 
         Label(root, text = "You clicked No button").pack()


def open(): 
    top = Toplevel()
    top.title("New window")
    closeWindowButton = Button(top, text= "Close Window", command= top.destroy).pack()



def show():
    myLabel = Label (root, text = selectItem.get()).pack()
    for text, mode in SelectOption: 
     Radiobutton(root, text=text, variable=choices, value=mode).pack(anchor=W)


def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()
    drop = OptionMenu (root, selectItem, *options)
    drop.pack()


#Disable Button

disabledButton = Button(root, text = "Press Button", state = DISABLED)
disabledButton.pack()


#Activate Button

activateButton = Button(root, text= "Press Button", padx = 50, pady = 50, command = ICLicked, fg="red")
activateButton.pack()



Button(root, text ="Text", command=popup).pack()
openWindowButton = Button(root, text = "Open new Window", command=open).pack()


#Dropdown button

myButton = Button(root, text="Select here", command=show).pack()


#Radio Button

myButton = Button(root, text="Kokeile!", command = lambda: clicked(choices.get()))
myButton.pack()


#Start window named root

root.mainloop()