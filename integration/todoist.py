from todoist_api_python.api import TodoistAPI
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

def deleteTask(taskID):
    api = apiCall()

    task = api.delete_task(task_id=f"{taskID}")

def completeTask(taskID):
    api = apiCall()

    task = api.close_task(task_id=f"{taskID}")

if __name__ == "__main__":
    pass