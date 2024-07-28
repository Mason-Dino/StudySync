import customtkinter

from task import getClassInfo

def classInfoScreen(self, id):
    classInfo = getClassInfo(id)

    print(classInfo)