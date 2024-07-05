from datetime import datetime
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

