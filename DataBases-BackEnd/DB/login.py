####################################
# Login System for Student Database
# Created by: Hamza Sahqani
####################################

import sqlite3


conn = sqlite3.connect("DataBases-BackEnd\DB\school.db")
c = conn.cursor()

c.execute("PRAGMA foreign_keys = ON")


# --- Create table ---

def create_table():
       # Login table (authentication)
    c.execute("""
        CREATE TABLE IF NOT EXISTS login(
            Username TEXT PRIMARY KEY COLLATE BINARY,
            Passwords TEXT
        )
    """)

    # Student table (structure)
    c.execute("""
        CREATE TABLE IF NOT EXISTS Student(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            birthday DATA,
            major TEXT,
            name REFERENCES login(Username)
        )
    """)

    conn.commit()

# --- Register (adds authorized users) ---
def register():
    username = input("Enter username (must match student name exactly): ")
    password = input("Enter password: ")

    # Check if student exists
    c.execute(
        "SELECT id FROM Student WHERE name=? COLLATE BINARY",
        (username,)
    )
    student = c.fetchone()

    if not student:
        print("❌ No matching student found. Cannot register.\n")
        return

    try:
        c.execute(
            "INSERT INTO login (Username, Passwords) VALUES (?, ?)",
            (username, password)
        )
        conn.commit()
        print("✅ Registered successfully.\n")

    except sqlite3.IntegrityError:
        print("❌ User already exists.\n")


# --- Login (ONLY if user exists exactly) ---
def login():
    username = input("Username: ")
    password = input("Password: ")

    c.execute("""
        SELECT login.Username
        FROM login
        JOIN Student ON login.Username = Student.name
        WHERE login.Username=? COLLATE BINARY
        AND login.Passwords=?
    """, (username, password))

    result = c.fetchone()

    if result:
        print(" Access granted! :) \n")
    else:
        print(" Access denied. :( \n")

def view_credits():
    username = input("Enter your username again to see how many credits your aah has: ")

    # Get student id
    c.execute(
        "SELECT id FROM Student WHERE name=? COLLATE BINARY",
        (username,)
    )
    student = c.fetchone()

    if not student:
        print("No such student.\n")
        return

    student_id = student[0]

    # Fetch credits
    c.execute("""
        SELECT Course.name, Credits.grade, Credits.credits
        FROM Credits
        JOIN Course ON Credits.id_course = Course.id
        WHERE Credits.id_student=?
    """, (student_id,))

    results = c.fetchall()

    if results:
        print("\nYour Credits:")
        for row in results:
            print(f"Course: {row[0]}, Grade: {row[1]}, Credits: {row[2]}")
        print()
    else:
        print("No credits found.\n")

# --- Menu ---
def menu():
    while True:
        print("====================================")
        print("Welcome to the Login System")
        print("====================================")
        print("1 - Register")
        print("2 - Login")
        print("0 - Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            register()
        elif choice == "2":
            login()
            Feed = input("View credits? (Yes/No): ").lower()
            if Feed == "yes":
                view_credits()
            elif Feed == "no":
                exit()
                break 
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Invalid option.\n")


if __name__ == "__main__":
 create_table()
 menu()

 conn.close()
