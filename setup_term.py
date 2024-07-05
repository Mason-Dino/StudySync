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

numClasses = int(input("How many classes do you have (max 10): "))

if numClasses > 10:
    print(f"Because you put {numClasses} classes it is set as 10")
    numClasses = 10

print("")

for i in range(numClasses):
    
