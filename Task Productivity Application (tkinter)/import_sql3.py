###########################################
# Task Productivity Application
# Author: Hamza Sahqani
# This is a simple task management & to-do list application built using Tkinter and SQLite.
# The application allows users to perform all CRUD functions (add, view, update, and delete tasks from a SQLite database.)
###########################################


from tkinter import *

import sqlite3


root = Tk()

root.title ("Tietokanta")

root.geometry("400x400")


conn = sqlite3.connect("tasklists.db")
c = conn.cursor()
c.execute ("DROP TABLE IF EXISTS tasks")

sql = '''CREATE TABLE tasks (
  task VARCHAR(255)

)'''

c.execute(sql)

conn.commit()

conn.close()


root.mainloop