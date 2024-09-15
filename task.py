import customtkinter
import datetime
import sqlite3
import json
import os

from integration.googleCal import *
from integration.todoist import *

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
        classID text,
        subLink text,
        ptsValue integer,
        importance integer,
        type text,
        googleCalID text,
        todoistID text
        )""")
    conn.commit()
    conn.close()

    if __name__ == "__main__":
        print("Database created successfully")

def deleteDatabase():
    if os.path.exists("study.db"):
        os.remove("study.db")

    database()

def makeTestTask():
    try:
        conn = sqlite3.connect('study.db')
        c = conn.cursor()

        c.execute("""INSERT INTO tasks VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", ("test123456789", "Birthday", 1, 2, 2006, 2012006, "None", "test", "test", "test", 10, 1, "test", "None", "None"))

        conn.commit()
        conn.close()

        conn = sqlite3.connect('study.db')
        c = conn.cursor()

    except:
        print("Error")

    c.execute("SELECT * FROM tasks")

    rows = c.fetchall()

    rows[0][12]

    conn.close()

    deleteTask("test123456789")

def addMainTask(taskName, taskID, className, classID, day, month, year, subLink, ptsValue, importance, type, todoistImport=False, todoistID: str = "None"):
    if ptsValue == "":
        ptsValue = "None"

    if int(day) < 10:
        daystr = "0" + str(day)

    else:
        daystr = str(day)

    if int(month) < 10:
        monthstr = "0" + str(month)

    else:
        monthstr = str(month)

    dateNum = int(f"{monthstr}" + f"{daystr}" + f"{year}")

    conn = sqlite3.connect('study.db')
    c = conn.cursor()

    googleCalID = "None"

    #def makeNewAssignment(name, year, month, day, classID):
    
    if checkIfGoogleCal() == True:
        print("make new assignment")
        event = makeNewAssignment(taskName, year, month, day, classID)
        googleCalID = event["id"]

    elif checkIfGoogleCal() == False:
        googleCalID = "None"

    if checkIfTodoist() == True and todoistImport == False:
        todoistID = makeTask(taskName, int(year), int(month), int(day), importance, classID)

        todoistID = str(todoistID.id)

    if todoistImport == True:
        todoistID = todoistID

    elif checkIfTodoist() == False:
        todoistID = "None"

    c.execute(f"INSERT INTO tasks VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (taskID, taskName, day, month, year, dateNum, "None", className, classID, subLink, ptsValue, importance, type, googleCalID, todoistID))
    
    conn.commit()
    conn.close()

def addSubTask(taskName, taskID, className, classID, day, month, year, parentID):
    conn = sqlite3.connect('study.db')
    c = conn.cursor()

    c.execute(f"SELECT * FROM tasks WHERE id = '{parentID}'")
    rows = c.fetchall()

    parTodoistID = rows[0][14]

    conn.commit()
    conn.close()

    if int(day) < 10:
        daystr = "0" + str(day)

    else:
        daystr = str(day)

    if int(month) < 10:
        monthstr = "0" + str(month)

    else:
        monthstr = str(month)
        
    dateNum = int(f"{monthstr}" + f"{daystr}" + f"{year}")

    conn = sqlite3.connect('study.db')
    c = conn.cursor()


    if checkIfTodoist() == True:
        todoistid = makeSubtask(parTodoistID, taskName, year, month, day)

        todoistid = str(todoistid.id)

    else:
        todoistid = "None"

    c.execute(f"INSERT INTO tasks VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (taskID, taskName, day, month, year, dateNum, parentID, className, classID, "None", "None", "None", "None", "None", todoistid))
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

def checkTaskByTodoistID(id):
    conn = sqlite3.connect('study.db')
    c = conn.cursor()

    c.execute(f"SELECT * FROM tasks WHERE todoistID = '{id}'")
    rows = c.fetchall()
    conn.close()

    if len(rows) == 0:
        api = apiCall()
        task = api.get_task(id)

        return "make task"

    
    else:
        api = apiCall()
        task = api.get_task(id)

        try:
            if task.is_completed == True:
                return "completed task"
            
            else:
                return "task"
            
        except:
            return "delete task"
        



    return rows

def getMainTaskSingle(id):
    conn = sqlite3.connect('study.db')
    c = conn.cursor()

    c.execute(f"SELECT * FROM tasks WHERE id = '{id}'")
    rows = c.fetchall()
    conn.close()

    return rows

def getSubTaskSingle(id):
    conn = sqlite3.connect('study.db')
    c = conn.cursor()

    c.execute(f"SELECT * FROM tasks WHERE id = '{id}'")
    rows = c.fetchall()
    conn.close()

    return rows

def getSubTasks(parentid):
    conn = sqlite3.connect('study.db')
    c = conn.cursor()

    c.execute(f"SELECT * FROM tasks WHERE parentID = '{parentid}'")
    rows = c.fetchall()
    conn.close()

    return rows

def getStudySubTasks():
    conn = sqlite3.connect('study.db')
    c = conn.cursor()

    c.execute(f"SELECT * FROM tasks WHERE parentID = 'StudyTimer'")
    rows = c.fetchall()
    conn.close()

    return rows

def getSubTaskParentID(id):
    conn = sqlite3.connect('study.db')
    c = conn.cursor()

    c.execute(f"SELECT parentID FROM tasks WHERE id = '{id}'")
    rows = c.fetchall()
    conn.close()

    return rows

def getClassTasks(classID):
    conn = sqlite3.connect('study.db')
    c = conn.cursor()

    c.execute(f"SELECT * FROM tasks WHERE classID = '{classID}' AND parentID='None' ORDER BY date ASC")
    rows = c.fetchall()
    conn.close()

    return rows

def finishMainTask(self, id):
    subTask = getSubTasks(id)
    mainTask = getMainTaskSingle(id)

    if len(subTask) > 0:
        for i in range(len(subTask)):
            completeTaskTodoist(subTask[i][14])
            finishSubTask(self, subTask[i][0])

    conn = sqlite3.connect('study.db')
    c = conn.cursor()

    completeTaskTodoist(mainTask[0][14])
    c.execute(f"DELETE FROM tasks WHERE id='{id}'")

    conn.commit()
    conn.close()
    
    before = self.progressbar.get()

    with open("setup.json", "r") as f:
        self.setupDir = json.load(f)

    self.progressbar.step()
    self.progressbar.step()

    after = self.progressbar.get()
    
    if before > after:
        self.setupDir["level"] += 1


    self.setupDir["progress"] = self.progressbar.get()

    with open("setup.json", "w") as f:
        json.dump(self.setupDir, f, indent=4)

def finishSubTask(self, id: str):
    subTask = getSubTaskSingle(id)

    conn = sqlite3.connect('study.db')
    c = conn.cursor()

    completeTaskTodoist(subTask[0][14])
    c.execute(f"DELETE FROM tasks WHERE id='{id}'")

    conn.commit()
    conn.close()

    before = self.progressbar.get()

    with open("setup.json", "r") as f:
        self.setupDir = json.load(f)

    self.progressbar.step()

    after = self.progressbar.get()
    
    if before > after:
        self.setupDir["level"] += 1

    self.setupDir["progress"] = self.progressbar.get()

    with open("setup.json", "w") as f:
        json.dump(self.setupDir, f, indent=4)

def searchDayTask(day: int, month: int, year: int = None):
    conn = sqlite3.connect('study.db')
    c = conn.cursor()

    if year == None:
        year = datetime.datetime.now().year

    c.execute(f"SELECT * FROM tasks WHERE day={day} AND month={month} AND year={year} and parentID='None'")
    rows = c.fetchall()
    conn.close()

    return rows

def getOverdueTasks():
    conn = sqlite3.connect('study.db')
    c = conn.cursor()

    c.execute(f"SELECT * FROM tasks WHERE date < {datetime.datetime.now().strftime('%m%d%Y')}")
    rows = c.fetchall()
    conn.close()

    return rows

def getTaskbyLevel(level: int):
    conn = sqlite3.connect('study.db')
    c = conn.cursor()

    c.execute(f"SELECT * FROM tasks WHERE importance={level} AND parentID='None'")
    rows = c.fetchall()
    conn.close()

    return rows

def editTask(id, type: str, value: str):
    conn = sqlite3.connect('study.db')
    c = conn.cursor()

    if type == "name":
        c.execute(f"UPDATE tasks SET task='{value}' WHERE id='{id}'")

    elif type == "date":
        value = value.split("/")
        day = int(value[1])
        month = int(value[0])
        year = int(value[2])

        if int(day) < 10:
            daystr = "0" + str(day)

        else:
            daystr = str(day)

        if int(month) < 10:
            monthstr = "0" + str(month)

        else:
            monthstr = str(month)

        dueDate = int(f"{monthstr}" + f"{daystr}" + f"{year}")

        c.execute(f"UPDATE tasks SET date={dueDate} WHERE id='{id}'")
        c.execute(f"UPDATE tasks SET day={day} WHERE id='{id}'")
        c.execute(f"UPDATE tasks SET month={month} WHERE id='{id}'")
        c.execute(f"UPDATE tasks SET year={year} WHERE id='{id}'")

        c.execute(f"UPDATE tasks SET date={dueDate} WHERE parentID='{id}'")
        c.execute(f"UPDATE tasks SET day={day} WHERE parentID='{id}'")
        c.execute(f"UPDATE tasks SET month={month} WHERE parentID='{id}'")
        c.execute(f"UPDATE tasks SET year={year} WHERE parentID='{id}'")

    elif type == "importance":
        c.execute(f"UPDATE tasks SET importance='{value}' WHERE id='{id}'")

    elif type == "submission":
        c.execute(f"UPDATE tasks SET subLink='{value}' WHERE id='{id}'")

    elif type == "points":
        c.execute(f"UPDATE tasks SET ptsValue='{value}' WHERE id='{id}'")

    elif type == "type":
        c.execute(f"UPDATE tasks SET type='{value}' WHERE id='{id}'")

    conn.commit()

    c.execute(f"SELECT * FROM tasks WHERE id='{id}'")

    row = c.fetchall()

    #editEvent(eventID, classID, summary, year, month, day):
    editEvent(row[0][13], row[0][8], row[0][1], row[0][4], row[0][3], row[0][2])

    conn.commit()
    conn.close()

def deleteTask(id):
    conn = sqlite3.connect('study.db')
    c = conn.cursor()

    c.execute(f"SELECT * FROM tasks WHERE id='{id}'")

    rows = c.fetchall()
    conn.commit()

    deleteTaskTodoist(rows[0][14])
    deleteEvent(rows[0][13], rows[0][8])

    c.execute(f"DELETE FROM tasks WHERE id='{id}'")
    conn.commit()

    subtask = getSubTasks(id)

    for i in range(len(subtask)):
        deleteTaskTodoist(subtask[i][14])

    c.execute(f"DELETE FROM tasks WHERE parentID='{id}'")
    conn.commit()

    conn.close()

def deleteSubTask(parentID):
    conn = sqlite3.connect('study.db')
    c = conn.cursor()

    c.execute(f"DELETE FROM tasks WHERE parentID='{parentID}'")

    conn.commit()
    conn.close()

def deleteOnlySubTask(id):
    subtask = getSubTaskSingle(id)

    conn = sqlite3.connect('study.db')
    c = conn.cursor()

    deleteTaskTodoist(subtask[0][14])

    c.execute(f"DELETE FROM tasks WHERE id='{id}'")

    conn.commit()
    conn.close()

def isLeapYear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
    
def getClassInfo(id):
    current = os.getcwd()

    with open(f"{current}/setup.json", "r") as f:
        setupDir = json.load(f)

    for i in range(setupDir["numClasses"]):
        if setupDir[f"class{i+1}"]["id"] == id:
            return setupDir[f"class{i+1}"]


if __name__ == "__main__":
    database()