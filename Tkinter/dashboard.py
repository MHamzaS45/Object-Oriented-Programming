# Avaa UI Kirjasto

from tkinter import ttk
import message_box as mb 
import tkinter as tk 
from tkinter.ttk import *
from tkinter import *
import customtkinter as ctk


def __init__(self, root):
 self._root = window
 self._entry = None


def start(self):
 heading_label = ttk.Label(master=self._root, text="Login")
 username_label = ttk.Label(master=self._root, text="Username")
 username_entry = ttk.Entry(master=self._root)
 password_label = ttk.Label(master=self._root, text="Password")
 password_entry = ttk.Entry(master=self._root)
 button = ttk.Button(master=self._root, text="Button")
 heading_label.grid(row=0, column=0, columnspan=2)
 username_label.grid(row=1, column=0)
 username_entry.grid(row=1, column=1)
 password_label.grid(row=2, column=0)
 password_entry.grid(row=2, column=1)
 button.grid(row=3, column=0, columnspan=2)

window = tk.Tk()
window.title(" Button Masher ") # What the application will be referred to as when booting
window.geometry("500x500")
window.configure(background="crimson")

window.rowconfigure(0, weight=1)

def IClicked():
    buttonClickLabel= Label(window, text="Nappulaa painettu!")
    buttonClickLabel.pack()

#disable the button
disableButton = Button(window, text="Paina nappulaa!", state=DISABLED)
disableButton.pack()

#aCTIVATE THE BUTTON
activateButton = Button(window, text="Paina nappulaa", padx = 50, pady = 50, command=IClicked, fg ="red")
activateButton.pack()

mb.Button(window, text="Show Message Box", command=mb.popup).pack()




window.mainloop()

