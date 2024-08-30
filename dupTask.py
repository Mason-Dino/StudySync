import json

tasks = [('4R7hQgwD1Rb6fecg4wZ0', 'Task', 26, 8, 2024, 8262024, 'None', 'None', '0000000000', 'None', 'None', 5, 'None'), ('593aw19KkX5DRiL6GXA2', 'lol', 26, 8, 2024, 8262024, 'None', 'Computer Science 1', 'cOspDDRuA7', 'None', 'None', 5, 'None')]

def findDupTask(tasks):
    dupTask = []

    for i in range(len(tasks)):
        counter = 0
        for c in range(len(tasks)):
            if tasks[i][1] == tasks[c][1]:
                counter += 1

        if counter > 1:
            dupTask.append((tasks[i][0], tasks[i][1], i))

    duplicate = {
        "groupNum": 1,
        "group1": []
        }

    if len(dupTask) == 0:
        return False
    
    else:
        duplicate["group1"].append(dupTask[0])

        groupNum = 1

        foundGroup = False

        for i in range(1, len(dupTask)):
            anotherGroup = False
            beforeGroupNum = duplicate["groupNum"]
            for j in range(duplicate["groupNum"]):
                if dupTask[i][1]  in duplicate[f"group{j+1}"][0][1]:
                    duplicate[f"group{j+1}"].append(dupTask[i])

                    anotherGroup = False
                    foundGroup = True

                else:
                    anotherGroup = True
                    foundGroup = False

                if foundGroup == True:
                    break


            if anotherGroup == True:
                groupNum += 1

                duplicate["groupNum"] = groupNum

                duplicate[f"group{groupNum}"] = [dupTask[i]]

        return duplicate

if __name__ == "__main__":
    print(json.dumps(findDupTask(tasks), indent=4))





