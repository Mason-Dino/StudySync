from datetime import datetime
import json

print("Welcome to Assignment Tracker!")
print("Today we are going to set up your experience!")
print("\n")

setup = {}

theme = input("What theme would you like (dark or light): ")

setup["theme"] = theme

print(setup)