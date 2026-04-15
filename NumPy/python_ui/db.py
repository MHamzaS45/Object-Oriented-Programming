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
