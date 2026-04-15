import tkinter as tk
from db import register, login, init_db
from views.matrix import MatrixView
from tkinter import messagebox

import sqlite3

def init_db():
    conn = sqlite3.connect("Data-Pipelines\\NumPy\\python_ui\\users.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
    conn.commit()
    conn.close()

def register(username, password):
    conn = sqlite3.connect("Data-Pipelines\\NumPy\\python_ui\\users.db")
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()

def login(username, password):
    conn = sqlite3.connect("Data-Pipelines\\NumPy\\python_ui\\users.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    result = c.fetchone()
    conn.close()
    return result

class LoginView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        init_db()

        tk.Label(self, text="Username").pack()
        self.username = tk.Entry(self)
        self.username.pack()

        tk.Label(self, text="Password").pack()
        self.password = tk.Entry(self, show="*")
        self.password.pack()

        tk.Button(self, text="Login", command=self.do_login).pack()
        tk.Button(self, text="Register", command=self.do_register).pack()

    def do_login(self):
        if login(self.username.get(), self.password.get()):
            import subprocess

            # Launch each feature as separate process
            subprocess.Popen(["python", "Data-Pipelines\\NumPy\\python_ui\\views\\rotate_square.py"])
            subprocess.Popen(["python", "Data-Pipelines\\NumPy\\python_ui\\views\\rotate_cube.py"])
            subprocess.Popen(["python", "Data-Pipelines\\NumPy\\python_ui\\views\\rockets.py"])
            subprocess.Popen(["python", "Data-Pipelines\\NumPy\\python_ui\\views\\matrix.py"])

    def do_register(self):
        register(self.username.get(), self.password.get())

