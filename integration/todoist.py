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
        className = []
        numClass = setup["numClasses"]
        todoistID = []
        todoistTaskID = []
        notTheSame = {}

        for i in range(numClass):
            classID.append(setup[f"class{i+1}"]["id"])
            className.append(setup[f"class{i+1}"]["name"])
            todoistID.append(str(setup["todoist"][setup[f"class{i+1}"]["id"]]["id"]))

        todoistID.append(str(setup["todoist"]["0000000000"]["id"]))
        classID.append("0000000000")
        className.append("None")

        studySyncTasks["info"]={}

        studySyncTasks["info"]["classID"] = classID
        studySyncTasks["info"]["className"] = className
        studySyncTasks["info"]["todoistID"] = todoistID

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
                    todoistTaskID.append(
                        {"id": task.id,
                        "parent_id": task.parent_id,
                        "location_id": task.section_id}
                                        )

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
                    todoistTaskID.append(
                        {"id": task.id,
                        "parent_id": task.parent_id,
                        "location_id": task.section_id}
                                        )

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
                    todoistTaskID.append(
                        {"id": task.id,
                        "parent_id": task.parent_id,
                        "location_id": task.project_id}
                                        )

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
                    todoistTaskID.append(
                        {"id": task.id,
                        "parent_id": task.parent_id,
                        "location_id": task.project_id}
                                        )

        from task import addMainTask, addSubTask, checkTaskByTodoistID
        from task import deleteTask, finishMainTask

        
        with open("studySync1.json", "w") as f:
            json.dump(studySyncTasks, f, indent=4)

        with open("studySync1.json", "r") as f:
            studySyncTasks = json.load(f)

        with open("studySync2.json", "r") as f:
            studySyncTasks2 = json.load(f)
        
        todoist1ID = studySyncTasks["info"]["todoistID"]
        todoist2ID = studySyncTasks2["info"]["todoistID"]

        contentChange = []
        subTaskChange = []
        dueChange = []
        priorityChange = []
        makeTasks = []

        for i in range(len(todoist1ID)):
            if studySyncTasks[todoist1ID[i]] != studySyncTasks2[todoist2ID[i]]:
                print("boo they suck, they arent th same")
                print(list(studySyncTasks[todoist1ID[i]].keys()))

                if len(list(studySyncTasks[todoist1ID[i]].keys())) == 0:
                    print("deleted task")

                for id in list(studySyncTasks[todoist1ID[i]].keys()):
                    try:
                        if studySyncTasks[todoist1ID[i]][id] != studySyncTasks2[todoist2ID[i]][id]:
                            if studySyncTasks[todoist1ID[i]][id]["content"] != studySyncTasks2[todoist2ID[i]][id]["content"]:
                                print("content")
                                contentChange.append(
                                    {"id": id,
                                    "location_id": todoist1ID[i],
                                    "content": studySyncTasks[todoist1ID[i]][id]["content"]}
                                )

                            if studySyncTasks[todoist1ID[i]][id]["subTasks"] != studySyncTasks2[todoist2ID[i]][id]["subTasks"]:
                                subTaskChange.append(
                                    {"id": id,
                                    "location_id": todoist1ID[i],
                                    "subTasks": studySyncTasks[todoist1ID[i]][id]["subTasks"]}
                                )

                            if studySyncTasks[todoist1ID[i]][id]["due"] != studySyncTasks2[todoist2ID[i]][id]["due"]:
                                dueChange.append(
                                    {"id": id,
                                    "location_id": todoist1ID[i],
                                    "due": studySyncTasks[todoist1ID[i]][id]["due"]}
                                )
                                print("due")

                            if studySyncTasks[todoist1ID[i]][id]["priority"] != studySyncTasks2[todoist2ID[i]][id]["priority"]:
                                print("priority")
                                priorityChange.append(
                                    {"id": id,
                                    "location_id": todoist1ID[i],
                                    "priority": studySyncTasks[todoist1ID[i]][id]["priority"]}
                                )

                        else:
                            print("they are th same")

                    except:
                        print("they are th same")
                        makeTasks.append({
                            "content": studySyncTasks[todoist1ID[i]][id]["content"],
                            "due": studySyncTasks[todoist1ID[i]][id]["due"],
                            "priority": studySyncTasks[todoist1ID[i]][id]["priority"],
                            "todoistClassID": todoist1ID[i],
                            "todoistID": id,
                            "subTasks": studySyncTasks[todoist1ID[i]][id]["subTasks"],
                            "classID": studySyncTasks["info"]["classID"][i],
                            "className": studySyncTasks["info"]["className"][i]
                            })

            elif studySyncTasks[todoist1ID[i]] == studySyncTasks2[todoist2ID[i]]:
                print("they are th same")
        
        
        print(contentChange)
        print(subTaskChange)
        print(dueChange)
        print(priorityChange)
        print(makeTasks)

        for task in makeTasks:
            parentTaskID = makeID(20)
            addMainTask(task["content"], parentTaskID, task["className"], task["classID"], task["due"].split("-")[2], task["due"].split("-")[1], task["due"].split("-")[0], "", "", task["priority"], "", True, task["todoistID"])

            if task["subTasks"] != {}:
                subTaskKey = list(task["subTasks"].keys())
                for i in range(len(task["subTasks"])):
                    subTask = task["subTasks"][subTaskKey[i]]
                    taskID = makeID(20)

                    addSubTask(subTask["content"], taskID, task["className"], task["classID"], task["due"].split("-")[2], task["due"].split("-")[1], task["due"].split("-")[0], parentTaskID, True, subTask["id"])

        for task in contentChange:
            updateTaskTodoist(task["id"], task["location_id"], "content",task["content"])
        
        
        
        with open("studySync2.json", "w") as f:
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

    if int(month) < 10:
        month = f"0{month}"

    if int(day) < 10:
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