import customtkinter

from task import getClassInfo
from themes.theme import topLevel

def classInfoScreen(self, id):
    classInfo = getClassInfo(id)

    self.content = customtkinter.CTkFrame(master=self)
    self.content.grid(row=0, column=1, rowspan=3, columnspan=2, sticky="nsew", padx=10, pady=10)
    self.content.grid_columnconfigure(0, weight=1)

    self.header = customtkinter.CTkLabel(master=self.content, text=f"{classInfo['name']} Class Info", font=customtkinter.CTkFont(size=20, weight="bold"))
    self.header.grid(row=0, column=0, sticky="nsew", padx=10, pady=7)

    self.classNameFrame = customtkinter.CTkFrame(master=self.content, corner_radius=6, fg_color=topLevel())
    self.classNameFrame.grid(row=1, column=0, sticky="nsew", padx=10, pady=7)
    self.classNameFrame.grid_columnconfigure((0,1), weight=1)

    self.className = customtkinter.CTkLabel(master=self.classNameFrame, text=f"Class Name:")
    self.className.grid(row=0, column=0, sticky="nsew", padx=10, pady=7)

    self.classNameLabel = customtkinter.CTkLabel(master=self.classNameFrame, text=f"{classInfo['name']}")
    self.classNameLabel.grid(row=0, column=1, sticky="nsew", padx=10, pady=7)

    self.classTeacherFrame = customtkinter.CTkFrame(master=self.content, corner_radius=6, fg_color=topLevel())
    self.classTeacherFrame.grid(row=2, column=0, sticky="nsew", padx=10, pady=7)
    self.classTeacherFrame.grid_columnconfigure((0,1), weight=1)

    self.classTeacher = customtkinter.CTkLabel(master=self.classTeacherFrame, text=f"Teacher: {classInfo['teacher']}")
    self.classTeacher.grid(row=0, column=0, sticky="nsew", padx=10, pady=7)

    self.classTeacherEmail = customtkinter.CTkLabel(master=self.classTeacherFrame, text=f"Teacher Email: {classInfo['email']}")
    self.classTeacherEmail.grid(row=1, column=0, sticky="nsew", padx=10, pady=7)

    self.displayFrame = customtkinter.CTkFrame(master=self.content, corner_radius=6, fg_color=topLevel())
    self.displayFrame.grid(row=3, column=0, sticky="nsew", padx=10, pady=7)
    self.displayFrame.grid_columnconfigure((0,1), weight=1)

    self.subject = customtkinter.CTkLabel(master=self.displayFrame, text=f"Subject: {classInfo['subject']}")
    self.subject.grid(row=0, column=0, sticky="nsew", padx=10, pady=7)

    self.icon = customtkinter.CTkLabel(master=self.displayFrame, text=f"Icon: {classInfo['icon']}")
    self.icon.grid(row=1, column=0, sticky="nsew", padx=10, pady=7)

    self.color = customtkinter.CTkLabel(master=self.displayFrame, text=f"Color: {classInfo['color']}")
    self.color.grid(row=2, column=0, sticky="nsew", padx=10, pady=7)
