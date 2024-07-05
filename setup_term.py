from datetime import datetime
from id import makeID
import json

print("Welcome to Assignment Tracker!")
print("Today we are going to set up your experience!")
print("")

setup = {}

mode = input("What mode would you like (dark or light): ")
setup["mode"] = mode

print(
    """Themes Available:
    \tBlue
    \tGreen
    \tOrange
    \tPurple
    \tREd
    \tTeal
    \tYellow
    \tGrey
    """)
theme = input("Please choose a theme from above: ")
setup["theme"] = theme

print("")
numClasses = int(input("How many classes do you have (max 10): "))

if numClasses > 10:
    print(f"Because you put {numClasses} classes it is set as 10")
    numClasses = 10

setup["numClass"] = numClasses

print("")

for i in range(numClasses):
    name = input("What is the class name: ")
    subject = input("What is the class subject: ")

    id = makeID()

    setup[f"class{i}"] = {}
    setup[f"class{i}"]["id"] = id
    setup[f"class{i}"]["name"] = name
    setup[f"class{i}"]["subject"] = subject

    print(f"you finished setting up {i + 1} class(es)")
    print("")


json_object = json.dumps(setup, indent=4)

with open("setup.json", "w") as outfile:
    outfile.write(json_object)

print("Assign Tracker is all setup!!")