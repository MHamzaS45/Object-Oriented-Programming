# Database Modification Functions
# Processing, Addition, Modification, Deletion

from dashboard import root
import tkinter as tk
from tkinter import *    

task_label = Label(root, text="Tehtävä")
task_label.grid(row=0, column=0, pady=(10,0))

task = Entry(root, width=30)
task.grid(row=0, column=1, padx = 20, pady=(10,0))

submit_button = Button(root, text = "Submit Task", command = submit)
submit_button.grid(row=2)