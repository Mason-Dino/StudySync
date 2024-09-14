from todoist_api_python.api import TodoistAPI
from id import makeID
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

def syncTodoist():
    if checkIfTodoist() == True:
        with open("setup.json", "r") as f:
            setup = json.load(f)

        api = apiCall()

        classID = []
        numClass = setup["numClasses"]
        todoistID = []

        for i in range(numClass):
            classID.append(setup[f"class{i+1}"]["id"])
            todoistID.append(str(setup["todoist"][setup[f"class{i+1}"]["id"]]["id"]))

        todoistID.append(str(setup["todoist"]["0000000000"]["id"]))

        print(todoistID)

        tasks = api.get_tasks()

        studySyncTasks = {}

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

        with open("studySync.json", "w") as f:
            json.dump(studySyncTasks, f, indent=4)

        from task import addMainTask, addSubTask

        for id in todoistID:
            for key in list(studySyncTasks[id].keys()):
                if studySyncTasks[id][key]["due"] == "None":
                    del studySyncTasks[id][key]

                else:
                    if studySyncTasks[id][key]["subTasks"] == {}:
                        taskID = makeID(20)

                        with open("setup.json", "r") as f:
                            setup = json.load(f)

                        for classID in classID:
                            if id == setup["todoist"][classID]["id"] or id == str(setup["todoist"]["0000000000"]["id"]):
                                if id == setup["todoist"][classID]["id"]:
                                    classIDS = classID

                                elif id == str(setup["todoist"]["0000000000"]["id"]):
                                    classIDS = "0000000000"
                                
                                for i in range(numClass):
                                    if classIDS == setup[f"class{i+1}"]["id"]:
                                        className = setup[f"class{i+1}"]["name"]
                                        break

                                    elif id == str(setup["todoist"]["0000000000"]["id"]):
                                        className = "None"
                                        break

                            else:
                                pass

                
                        #addMainTask(taskName, taskID, className, classID, day, month, year, subLink, ptsValue, importance, type):
                        
                        addMainTask(
                            studySyncTasks[id][key]["content"],
                            taskID,
                            className,
                            classIDS,
                            studySyncTasks[id][key]["due"].split("-")[2],
                            studySyncTasks[id][key]["due"].split("-")[1],
                            studySyncTasks[id][key]["due"].split("-")[0],
                            "", "", 4, "",
                            True, studySyncTasks[id][key]["id"]
                        )
                        
                        pass

                    else:
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