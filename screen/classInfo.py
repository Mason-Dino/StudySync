import customtkinter

from task import getClassInfo
from themes.theme import topLevel

def classInfoScreen(self, id):
    classInfo = getClassInfo(id)

    self.content = customtkinter.CTkFrame(master=self)
    self.content.grid(row=0, column=1, rowspan=3, columnspan=2, sticky="nsew", padx=10, pady=10)
    self.content.grid_columnconfigure(0, weight=1)

    self.className = customtkinter.CTkLabel(master=self.content, text=f"Class Name: {classInfo['name']}")
    self.className.grid(row=0, column=0, sticky="nsew", padx=10, pady=7)

    self.classTeacher = customtkinter.CTkLabel(master=self.content, text=f"Teacher: {classInfo['teacher']}")
    self.classTeacher.grid(row=1, column=0, sticky="nsew", padx=10, pady=7)

    self.classTeacherEmail = customtkinter.CTkLabel(master=self.content, text=f"Teacher Email: {classInfo['email']}")
    self.classTeacherEmail.grid(row=2, column=0, sticky="nsew", padx=10, pady=7)

    self.subject = customtkinter.CTkLabel(master=self.content, text=f"Subject: {classInfo['subject']}")
    self.subject.grid(row=3, column=0, sticky="nsew", padx=10, pady=7)

    self.icon = customtkinter.CTkLabel(master=self.content, text=f"Icon: {classInfo['icon']}")
    self.icon.grid(row=4, column=0, sticky="nsew", padx=10, pady=7)
