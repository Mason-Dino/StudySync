from todoist_api_python.api import TodoistAPI
from id import makeID
import sqlite3
import json

def checkIfTodoist():
    with open("setup.json", "r") as f:
        setup = json.load(f)

    
    try:
        if setup["todoistSetup"] == True:
            return True
        else:
            return False
        
    except:
        setup["todoistSetup"] = False
        with open("setup.json", "w") as f:
            json.dump(setup, f, indent=4)

        return False

def apiCall():
    with open("setup.json", "r") as f:
        setup = json.load(f)

    token = setup["todoist"]["token"]

    api = TodoistAPI(token)
    return api

def syncTodoist(self):
    if checkIfTodoist() == True:
        with open("setup.json", "r") as f:
            setup = json.load(f)

        api = apiCall()

        tasks = api.get_tasks()

        studySyncTasks = {}

        classID = []
        numClass = setup["numClasses"]
        todoistID = []
        todoistTaskID = []
        makeTodoistTaskID = []
        nothingTodoist = []

        for i in range(numClass):
            classID.append(setup[f"class{i+1}"]["id"])
            todoistID.append(str(setup["todoist"][setup[f"class{i+1}"]["id"]]["id"]))

        todoistID.append(str(setup["todoist"]["0000000000"]["id"]))

        for id in todoistID:
            studySyncTasks[id] = {}

        for task in tasks:
            if task.due == None:
                due = "None"

            else:
                due = task.due.date

            if task.section_id in todoistID:
                try:
                    studySyncTasks[f"{task.section_id}"][task.parent_id]["subTasks"][task.id] = {
                        "content": task.content,
                        "description": task.description,
                        "due": due,
                        "priority": task.priority,
                        "project_id": task.project_id,
                        "section_id": task.section_id,
                        "parent_id": task.parent_id,
                        "id": task.id
                    }
                    todoistTaskID.append(task.id)

                except:
                    studySyncTasks[f"{task.section_id}"][task.id] = {
                        "content": task.content,
                        "description": task.description,
                        "due": due,
                        "priority": task.priority,
                        "project_id": task.project_id,
                        "section_id": task.section_id,
                        "parent_id": task.parent_id,
                        "id": task.id,
                        "subTasks": {}
                    }
                    todoistTaskID.append(task.id)

            elif task.project_id in todoistID:
                try:
                    studySyncTasks[f"{task.project_id}"][task.parent_id]["subTasks"][task.id] = {
                        "content": task.content,
                        "description": task.description,
                        "due": due,
                        "priority": task.priority,
                        "project_id": task.project_id,
                        "section_id": task.section_id,
                        "parent_id": task.parent_id,
                        "id": task.id
                    }
                    todoistTaskID.append(task.id)

                except:
                    studySyncTasks[f"{task.project_id}"][task.id] = {
                        "content": task.content,
                        "description": task.description,
                        "due": due,
                        "priority": task.priority,
                        "project_id": task.project_id,
                        "section_id": task.section_id,
                        "parent_id": task.parent_id,
                        "id": task.id,
                        "subTasks": {}
                    }
                    todoistTaskID.append(task.id)

        from task import addMainTask, addSubTask, checkTaskByTodoistID
        from task import deleteTask, finishMainTask


        conn = sqlite3.connect('study.db')
        c = conn.cursor()

        c.execute("SELECT * FROM tasks")
        rows = c.fetchall()

        conn.close()

        for row in rows:
            if row[14] in todoistTaskID:
                pass
            else:
                todoistTaskID.append(row[14])
        
        with open("studySync.json", "w") as f:
            json.dump(studySyncTasks, f, indent=4)

        for id in todoistTaskID:
            print(checkTaskByTodoistID(id))

            if checkTaskByTodoistID(id) == "make task":
                makeTodoistTaskID.append(id)

            elif checkTaskByTodoistID(id) == "task":
                nothingTodoist.append(id)

        #tasks = api.get_tasks(ids=todoistTaskID)

        #print(tasks)
        print(makeTodoistTaskID)
        print(nothingTodoist)

        for task in nothingTodoist:
            for id in todoistID:
                try:
                    del studySyncTasks[f"{id}"][task]

                except:
                    pass

        with open("studySync.json", "w") as f:
            json.dump(studySyncTasks, f, indent=4)

        

    else:
        pass

def makeTask(taskName, year, month, day, priority, classID):
    api = apiCall()

    with open("setup.json", "r") as f:
        setup = json.load(f)

    todoist = setup["todoist"][classID]

    if priority == 1:
        priority = 4

    elif priority == 2:
        priority = 3

    elif priority == 3:
        priority = 2

    elif priority == 4 or priority == 5:
        priority = 1

    if month < 10:
        month = f"0{month}"

    if day < 10:
        day = f"0{day}"

    if todoist["type"] == "section":
        task = api.add_task(
            content=f"{taskName}",
            description=f"Imported from StudySync",
            due_date=f"{year}-{month}-{day}",
            section_id=todoist["id"],
            priority=priority,
        )

    elif todoist["type"] == "project":
        task = api.add_task(
            content=f"{taskName}",
            description=f"Imported from StudySync",
            due_date=f"{year}-{month}-{day}",
            project_id=todoist["id"],
            priority=priority,
        )

    print("make task")
    return task

def makeSubtask(taskID, taskName, year, month, day):
    api = apiCall()

    if month < 10:
        month = f"0{month}"

    if day < 10:
        day = f"0{day}"

    task = api.add_task(
        content=f"{taskName}",
        description=f"Imported from StudySync",
        due_date=f"{year}-{month}-{day}",
        parent_id=taskID,
        priority=1,
    )
    print("make sub task")
    return task

def editTask(taskID, taskName, year, month, day, priority, type):
    api = apiCall()

    if month < 10:
        month = f"0{month}"

    if day < 10:
        day = f"0{day}"

    if type.lower() == "main":
        if priority == 1:
            priority = 4

        elif priority == 2:
            priority = 3

        elif priority == 3:
            priority = 2

        elif priority == 4 or priority == 5:
            priority = 1

    task = api.update_task(
        task_id=f"{taskID}",
        content=f"{taskName}",
        due_date=f"{year}-{month}-{day}",
        priority=priority
    )

    return task

def deleteTaskTodoist(taskID):
    api = apiCall()

    task = api.delete_task(task_id=f"{taskID}")

def completeTaskTodoist(taskID):
    api = apiCall()

    task = api.close_task(task_id=f"{taskID}")

    return "done"

if __name__ == "__main__":
    syncTodoist()