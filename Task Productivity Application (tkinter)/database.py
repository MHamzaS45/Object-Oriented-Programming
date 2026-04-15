from tkinter import *
import sqlite3

# ------------------ MAIN WINDOW ------------------
root = Tk()
root.title("Tietokanta")
root.geometry("400x400")

query_label = Label(root)

# ------------------ DATABASE FUNCTIONS ------------------

def query():
    conn = sqlite3.connect("tasklists.db")
    c = conn.cursor()

    c.execute("SELECT task, oid FROM tasks")
    records = c.fetchall()

    print_records = ''
    for record in records:
        print_records += str(record[0] + "\t" + str(record[1])) + "\n"

    heading_label = Label(root, text="Helvetica", font=("Helvetica", 16))
    heading_label['text'] = "Tehtava \t ID"
    heading_label.grid(row=7, column=0, columnspan=2)

    query_label['text'] = print_records
    query_label.grid(row=8, column=0, columnspan=2)

    conn.commit()
    conn.close()


def submit():
    conn = sqlite3.connect("tasklists.db")
    c = conn.cursor()

    c.execute("INSERT INTO tasks VALUES (:task)", {
        'task': task.get()
    })

    conn.commit()
    conn.close()

    task.delete(0, END)


def delete():
    conn = sqlite3.connect("tasklists.db")
    c = conn.cursor()

    c.execute("DELETE FROM tasks WHERE oid=" + delete_box.get())

    delete_box.delete(0, END)

    conn.commit()
    conn.close()


def update():
    conn = sqlite3.connect("tasklists.db")
    c = conn.cursor()

    record_id = delete_box.get()

    c.execute("""UPDATE tasks SET
                task = :task
                WHERE oid = :oid""", {
        'task': task_editor.get(),
        'oid': record_id
    })

    conn.commit()
    conn.close()

    editor.destroy()


# ------------------ EDIT WINDOW ------------------

def edit():
    global editor
    editor = Tk()
    editor.title("Paivita")
    editor.geometry("400x400")

    conn = sqlite3.connect("tasklists.db")
    c = conn.cursor()

    record_id = delete_box.get()
    c.execute("SELECT * FROM tasks WHERE oid = " + record_id)
    records = c.fetchall()

    global task_editor

    task_label = Label(editor, text="Tehtava")
    task_label.grid(row=0, column=0, pady=(10, 0))

    task_editor = Entry(editor, width=30)
    task_editor.grid(row=0, column=1, padx=20, pady=(10, 0))

    for record in records:
        task_editor.insert(0, record[0])

    save_btn = Button(editor, text="Tallenna", command=update)
    save_btn.grid(row=2, column=0, columnspan=2, pady=10, padx=10)


# ------------------ UI ELEMENTS ------------------

task_label = Label(root, text="Task")
task_label.grid(row=0, column=0, pady=(10, 0))

task = Entry(root, width=30)
task.grid(row=0, column=1, padx=20, pady=(10, 0))

submit_btn = Button(root, text="Add new task into Database", command=submit)
submit_btn.grid(row=2, column=0, columnspan=2, pady=10, padx=10)

query_btn = Button(root, text="Show task", command=query)
query_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10)

select_label = Label(root, text="Select ID")
select_label.grid(row=4, column=0, pady=5)

delete_box = Entry(root, width=30)
delete_box.grid(row=4, column=1, pady=5)

delete_btn = Button(root, text="Remove task", command=delete)
delete_btn.grid(row=5, column=0, columnspan=2, pady=10, padx=10)

edit_btn = Button(root, text="Edit task", command=edit)
edit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10)


# ------------------ MAIN LOOP ------------------

root.mainloop()
