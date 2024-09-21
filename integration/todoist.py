from tkinter import messagebox
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
    print("start--------------------------------------------------------------------")
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

        try:

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
                        if due == "None":
                            pass
                        else:
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
                        if due == "None":
                            pass
                        else:
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
            from task import deleteTask, finishMainTask, updateSubTaskfromTodoist

            
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
            delComplete = []

            for i in range(len(todoist1ID)):
                if studySyncTasks[todoist1ID[i]] != studySyncTasks2[todoist2ID[i]]:
                    print("boo they suck, they arent th same")
                    print(list(studySyncTasks[todoist1ID[i]].keys()))

                    if len(list(studySyncTasks[todoist1ID[i]].keys())) == 0:
                        for id in list(studySyncTasks2[todoist2ID[i]].keys()):
                            delComplete.append({"id": id, "location_id": todoist1ID[i]})

                    elif len(list(studySyncTasks[todoist1ID[i]].keys())) != len(list(studySyncTasks2[todoist2ID[i]].keys())):
                        print("hry")
                        listID1 = list(studySyncTasks[todoist1ID[i]].keys())
                        listID2 = list(studySyncTasks2[todoist2ID[i]].keys())

                        for id in listID1:
                            if id not in listID2:
                                delComplete.append({"id": id, "location_id": todoist1ID[i]})

                        for id in listID2:
                            if id not in listID1:
                                delComplete.append({"id": id, "location_id": todoist2ID[i]})

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
                            if studySyncTasks[todoist1ID[i]][id]["due"] == "None":
                                pass

                            else:
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
            print(delComplete)

            for task in makeTasks:
                parentTaskID = makeID(20)

                priority = int(task["priority"])

                if priority == 1:
                    priority = 4

                elif priority == 2:
                    priority = 3

                elif priority == 3:
                    priority = 2

                elif priority == 4 or priority == 5:
                    priority = 1
                try:
                    addMainTask(task["content"], parentTaskID, task["className"], task["classID"], task["due"].split("-")[2], task["due"].split("-")[1], task["due"].split("-")[0], "", "", priority, "", True, task["todoistID"])
                except:
                    pass

                if task["subTasks"] != {}:
                    subTaskKey = list(task["subTasks"].keys())
                    for i in range(len(task["subTasks"])):
                        subTask = task["subTasks"][subTaskKey[i]]
                        taskID = makeID(20)

                        addSubTask(subTask["content"], taskID, task["className"], task["classID"], task["due"].split("-")[2], task["due"].split("-")[1], task["due"].split("-")[0], parentTaskID, True, subTask["id"])

            for task in contentChange:
                updateTaskFromTodoist(task["id"], task["location_id"], "content", task["content"])

            for task in priorityChange:
                updateTaskFromTodoist(task["id"], task["location_id"], "priority", task["priority"])

            for task in dueChange:
                print(task["due"])
                updateTaskFromTodoist(task["id"], task["location_id"], "due", task["due"])

            from task import getTaskfromTodoist
            

            for task in subTaskChange:
                print(task)
                subTaskID = list(task["subTasks"].keys())
                subTaskID2 = list(studySyncTasks2[task["location_id"]][task["id"]]["subTasks"].keys())
                print(subTaskID2)
                print("hey12")
                print(subTaskID)

                for id in subTaskID2:
                    if id not in subTaskID:
                        delComplete.append({"id": id, "location_id": task["location_id"]})

                    else:
                        pass

                for i in range(len(subTaskID)):
                    subTaskTodoistID = subTaskID[i]

                    error1 = True
                    error2 = True

                    try:
                        studySyncTasks[task["location_id"]][task["id"]]["subTasks"][subTaskTodoistID]
                        error1 = False
                        
                    except:
                        pass


                    try:
                        studySyncTasks2[task["location_id"]][task["id"]]["subTasks"][subTaskTodoistID]
                        error2 = False

                    except:
                        pass

                    if error1 == False and error2 == False:
                        if studySyncTasks[task["location_id"]][task["id"]]["subTasks"][subTaskTodoistID]["content"] != studySyncTasks2[task["location_id"]][task["id"]]["subTasks"][subTaskTodoistID]["content"]:
                            updateSubTaskfromTodoist(subTaskTodoistID, "content", studySyncTasks[task["location_id"]][task["id"]]["subTasks"][subTaskTodoistID]["content"])

                    elif error1 == False and error2 == True:
                        row = getTaskfromTodoist(task["id"])
                        #addSubTask(taskName, taskID, className, classID, day, month, year, parentID, todoistImport=False, todoistID: str = "None"):
                        name = studySyncTasks[task["location_id"]][task["id"]]["subTasks"][subTaskTodoistID]["content"]
                        taskID = makeID(20)
                        className = row[0][7]
                        classID = row[0][8]
                        day = studySyncTasks[task["location_id"]][task["id"]]["due"].split("-")[2]
                        month = studySyncTasks[task["location_id"]][task["id"]]["due"].split("-")[1]
                        year = studySyncTasks[task["location_id"]][task["id"]]["due"].split("-")[0]
                        parentID = row[0][0]
                        todoistImport = True
                        todoistID = subTaskTodoistID
                        addSubTask(name, taskID, className, classID, day, month, year, parentID, todoistImport, todoistID)

                    elif error1 == True and error2 == True:
                        print("delete or complete")

            for task in delComplete:
                result = checkTaskByTodoistID(task["id"])

                if result == "completed task":
                    row = getTaskfromTodoist(task["id"])
                    finishMainTask(self, row[0][0])

                elif result == "delete task":
                    row = getTaskfromTodoist(task["id"])
                    deleteTask(row[0][0])
                    
                    
            
            with open("studySync2.json", "w") as f:
                json.dump(studySyncTasks, f, indent=4)

            print("end--------------------------------------------------------")

        except Exception as e:
            print(e)
            print("error")
            messagebox.showwarning("Error", "Please update the Todoist setup!!")

        

    else:
        pass

def makeTask(taskName, year, month, day, priority, classID):
    api = apiCall()

    with open("setup.json", "r") as f:
        setup = json.load(f)

    with open("studySync2.json", "r") as f:
        studySyncTasks2 = json.load(f)

    try:

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

            studySyncTasks2[f"{task.section_id}"][task.id] = {
                "content": task.content,
                "description": task.description,
                "due": f"{year}-{month}-{day}",
                "priority": task.priority,
                "project_id": task.project_id,
                "section_id": task.section_id,
                "parent_id": task.parent_id,
                "id": task.id,
                "subTasks": {}
            }

        elif todoist["type"] == "project":
            task = api.add_task(
                content=f"{taskName}",
                description=f"Imported from StudySync",
                due_date=f"{year}-{month}-{day}",
                project_id=todoist["id"],
                priority=priority,
            )

            studySyncTasks2[f"{task.project_id}"][task.id] = {
                "content": task.content,
                "description": task.description,
                "due": f"{year}-{month}-{day}",
                "priority": task.priority,
                "project_id": task.project_id,
                "section_id": task.section_id,
                "parent_id": task.parent_id,
                "id": task.id,
                "subTasks": {}
            }

        with open("studySync2.json", "w") as f:
            json.dump(studySyncTasks2, f, indent=4)

        print("make task")
        return task
    
    except:
        messagebox.showwarning("Error", "Please update the Todoist setup!!")
        print("error")


def makeSubtask(taskID, taskName, year, month, day):
    api = apiCall()

    with open("setup.json", "r") as f:
        setup = json.load(f)

    with open("studySync2.json", "r") as f:
        studySyncTasks2 = json.load(f)

    if int(month) < 10:
        month = f"0{month}"

    if int(day) < 10:
        day = f"0{day}"

    task = api.add_task(
        content=f"{taskName}",
        description=f"Imported from StudySync",
        parent_id=taskID,
        priority=1,
    )

    todoistID = studySyncTasks2["info"]["todoistID"]

    if task.section_id in todoistID:
        studySyncTasks2[f"{task.section_id}"][task.parent_id]["subTasks"][task.id] = {
            "content": task.content,
            "description": task.description,
            "due": "None",
            "priority": task.priority,
            "project_id": task.project_id,
            "section_id": task.section_id,
            "parent_id": task.parent_id,
            "id": task.id
        }

    elif task.project_id in todoistID:
        studySyncTasks2[f"{task.project_id}"][task.parent_id]["subTasks"][task.id] = {
            "content": task.content,
            "description": task.description,
            "due": "None",
            "priority": task.priority,
            "project_id": task.project_id,
            "section_id": task.section_id,
            "parent_id": task.parent_id,
            "id": task.id
        }

    with open("studySync2.json", "w") as f:
        json.dump(studySyncTasks2, f, indent=4)

    print("make sub task")
    return task

def editTask(taskID, taskName, year, month, day, priority):
    api = apiCall()

    if month < 10:
        month = f"0{month}"

    if day < 10:
        day = f"0{day}"

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

def updateTaskFromTodoist(taskID, locationID, type, content):
    from task import updateTaskByTodoist

    if type.lower() == "content":
        updateTaskByTodoist(taskID, type, content)

    if type.lower() == "priority":
        updateTaskByTodoist(taskID, type, content)

    if type.lower() == "due":
        updateTaskByTodoist(taskID, type, content)

def deleteTaskTodoist(taskID):
    try:
        api = apiCall()

        task = api.delete_task(task_id=f"{taskID}")

    except:
        pass

def completeTaskTodoist(taskID):
    try:
        api = apiCall()

        task = api.close_task(task_id=f"{taskID}")

        return "done"
    
    except:
        return "error"

def ProjectorSection(id):
    api = apiCall()

    try:
        section = api.get_section(id)

        return "section"
    
    except:
        try:
            project = api.get_project(id)

            return "project"
        
        except:
            return "None"


if __name__ == "__main__":
    syncTodoist()