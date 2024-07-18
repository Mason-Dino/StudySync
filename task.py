import customtkinter
import sqlite3
import json

def database():
    conn = sqlite3.connect('study.db')
    c = conn.cursor()
    
    c.execute("""CREATE TABLE IF NOT EXISTS tasks (
        id text PRIMARY KEY,
        task text,
        day integer,
        month integer,
        year integer,
        date integer,
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
    dateNum = int(f"{month}" + f"{day}" + f"{year}")

    conn = sqlite3.connect('study.db')
    c = conn.cursor()

    c.execute(f"INSERT INTO tasks VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (taskID, taskName, day, month, year, dateNum, "None", className, classID))
    conn.commit()
    conn.close()

def getMainTasks(organize: str = None):
    conn = sqlite3.connect('study.db')
    c = conn.cursor()

    if organize == None:
        organize = ""

    c.execute(f"SELECT * FROM tasks WHERE parentID = 'None' {organize}")
    rows = c.fetchall()
    conn.close()

    return rows

def finishMainTask(self, id):
    conn = sqlite3.connect('study.db')
    c = conn.cursor()

    c.execute(f"DELETE FROM tasks WHERE id='{id}'")

    conn.commit()
    conn.close()
    
    before = self.progressbar.get()

    with open("setup.json", "r") as f:
        self.setupDir = json.load(f)

    self.progressbar.step()
    self.progressbar.step()

    after = self.progressbar.get()
    print(before, after)
    if before > after:
        self.setupDir["level"] += 1
        print("level up")


    self.setupDir["progress"] = self.progressbar.get()

    with open("setup.json", "w") as f:
        json.dump(self.setupDir, f, indent=4)


if __name__ == "__main__":
    database()