# Radio Button 

from tkinter import *
root = Tk()
root.title("Radio Buttons")

SelectOption = [
    ("Selection 1", " Breaking Bad"),
    ("Selection 2", " The Soprnaos"),
    ("Selection 3", " The Wire"),
    ("Selection 4", " Death Note"),
    ("Selection 5", " Game of Thrones")
]

choices = StringVar()
choices.set(" Selection 1")

for text, mode in SelectOption:
    Radiobutton(root, text=text, variable=choices, value=mode).pack(anchor=W)

def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()

myButton = Button(root, text="Show Selection", command=lambda: clicked(choices.get()))
myButton.pack()

root.mainloop()
