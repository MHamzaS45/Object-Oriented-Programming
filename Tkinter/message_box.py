from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Message Box")

def popup():   
    response = messagebox.askyesno("Popup", "Do you want to continue?")
    # print(response) # Returns True if yes, False if no
    if response == 1:
        Label(root , text="You clicked yes!").pack()
    else: 
        Label(root , text="You clicked no!").pack()
    
# Create a button to show the message box
Button(root, text="Click Message", command=popup).pack()
root.mainloop()

