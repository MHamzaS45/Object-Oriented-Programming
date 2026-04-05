from tkinter import *

root = Tk()

def open():
    top = Toplevel()
    top.title("New Window")
    closeWindowButton = Button(top, text="Close Window", command=top.destroy).pack()

openWindowButton = Button(root, text="Open New Window", command=open).pack()

root.mainloop()
