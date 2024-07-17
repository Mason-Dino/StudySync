import customtkinter
import sqlite3

def database():
    conn = sqlite3.connect('study.db')
    c = conn.cursor()
    
    c.execute("""CREATE TABLE IF NOT EXISTS tasks (
        id text PRIMARY KEY,
        task text,
        day integer,
        month integer,
        year integer,
        parentID text,
        ClassName text,
        classID text
        )""")
    conn.commit()
    conn.close()

    if __name__ == "__main__":
        print("Database created successfully")

def addMainTask(taskName, taskID, className, classID, day, month, year):
    print(taskName, taskID, className, classID, day, month, year)

    conn = sqlite3.connect('study.db')
    c = conn.cursor()

    c.execute(f"INSERT INTO tasks VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (taskID, taskName, day, month, year, "None", className, classID))
    conn.commit()
    conn.close()

def getMainTasks():
    conn = sqlite3.connect('study.db')
    c = conn.cursor()

    c.execute("SELECT * FROM tasks WHERE parentID = 'None'")
    rows = c.fetchall()
    conn.close()

    return rows

if __name__ == "__main__":
    database()