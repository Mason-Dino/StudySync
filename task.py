import customtkinter
import sqlite3

def datebase():
    conn = sqlite3.connect('study.db')
    c = conn.cursor()
    
    c.execute("""CREATE TABLE IF NOT EXISTS tasks (
        id integer PRIMARY KEY,
        task text,
        due text,
        parentID text,
        classID text,
        )""")
    conn.commit()
    conn.close()

def addMainTask(taskName, taskID, className, classID, day, month, year):
    print(taskName, taskID, className, classID, day, month, year)