from tkinter import *
import sqlite3

root = Tk()
root.title("Database")
root.geometry("420x420")

# Connect to database
conn = sqlite3.connect("tasklist.db")
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS tasks")

sql = ''' CREATE TABLE tasks (id INTEGER PRIMARY KEY, 
 name TEXT NOT NULL, occupation TEXT NOT NULL, TaskPending BOOLEAN NOT NULL,
 Tasks TEXT ) '''

c.execute(sql)



