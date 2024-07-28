import customtkinter

from task import getClassInfo
from themes.theme import topLevel, loadColor
from icon import loadIcon
from screen.classAddEdit import classAddEdit

def classInfoScreen(self, id):
    classInfo = getClassInfo(id)

    infoFramepady = 6

    self.content = customtkinter.CTkFrame(master=self)
    self.content.grid(row=0, column=1, rowspan=3, columnspan=2, sticky="nsew", padx=10, pady=10)
    self.content.grid_columnconfigure(0, weight=1)
    self.content.grid_rowconfigure(1, weight=1)

    self.header = customtkinter.CTkLabel(master=self.content, text=f"{classInfo['name']} Class Info", font=customtkinter.CTkFont(size=20, weight="bold"))
    self.header.grid(row=0, column=0, sticky="nsew", padx=10, pady=3)

    self.infoFrame = customtkinter.CTkFrame(master=self.content, corner_radius=6, fg_color=topLevel())
    self.infoFrame.grid(row=1, column=0, sticky="nsew", padx=10, pady=7)
    self.infoFrame.grid_columnconfigure((0,1), weight=1)

    self.className = customtkinter.CTkLabel(master=self.infoFrame, text=f"Class Name:")
    self.className.grid(row=0, column=0, sticky="nsew", padx=10, pady=infoFramepady)

    self.classNameLabel = customtkinter.CTkLabel(master=self.infoFrame, text=f"{classInfo['name']}")
    self.classNameLabel.grid(row=0, column=1, sticky="nsew", padx=10, pady=infoFramepady)

    self.classTeacher = customtkinter.CTkLabel(master=self.infoFrame, text=f"Teacher:")
    self.classTeacher.grid(row=1, column=0, sticky="nsew", padx=10, pady=infoFramepady)

    self.classTeacher2 = customtkinter.CTkLabel(master=self.infoFrame, text=f"{classInfo['teacher']}")
    self.classTeacher2.grid(row=1, column=1, sticky="nsew", padx=10, pady=infoFramepady)

    self.classTeacherEmail = customtkinter.CTkLabel(master=self.infoFrame, text=f"Email:")
    self.classTeacherEmail.grid(row=2, column=0, sticky="nsew", padx=10, pady=infoFramepady)

    self.classTeacherEmail2 = customtkinter.CTkLabel(master=self.infoFrame, text=f"{classInfo['email']}")
    self.classTeacherEmail2.grid(row=2, column=1, sticky="nsew", padx=10, pady=infoFramepady)

    self.subject = customtkinter.CTkLabel(master=self.infoFrame, text=f"Subject:")
    self.subject.grid(row=3, column=0, sticky="nsew", padx=10, pady=infoFramepady)

    self.subject2 = customtkinter.CTkLabel(master=self.infoFrame, text=f"{classInfo['subject']}")
    self.subject2.grid(row=3, column=1, sticky="nsew", padx=10, pady=infoFramepady)

    self.icon = customtkinter.CTkLabel(master=self.infoFrame, text=f"Icon:")
    self.icon.grid(row=4, column=0, sticky="nsew", padx=10, pady=infoFramepady)

    self.icon2 = customtkinter.CTkLabel(master=self.infoFrame, image=loadIcon(classInfo['icon']), text="")
    self.icon2.grid(row=4, column=1, sticky="nsew", padx=10, pady=infoFramepady)

    self.color = customtkinter.CTkLabel(master=self.infoFrame, text=f"Color:")
    self.color.grid(row=5, column=0, sticky="nsew", padx=10, pady=infoFramepady)

    self.color2 = customtkinter.CTkFrame(master=self.infoFrame, fg_color=loadColor(classInfo['color']), width=30, height=20)
    self.color2.grid(row=5, column=1, sticky="nsew", padx=10, pady=infoFramepady)

    self.classID = customtkinter.CTkLabel(master=self.infoFrame, text=f"Class ID:")
    self.classID.grid(row=6, column=0, sticky="nsew", padx=10, pady=infoFramepady)

    self.classID2 = customtkinter.CTkLabel(master=self.infoFrame, text=f"{classInfo['id']}")
    self.classID2.grid(row=6, column=1, sticky="nsew", padx=10, pady=infoFramepady)

    self.buttonFrame = customtkinter.CTkFrame(master=self.content, corner_radius=6, fg_color=topLevel())
    self.buttonFrame.grid(row=2, column=0, sticky="nsew", padx=10, pady=3)
    self.buttonFrame.grid_columnconfigure((0, 1), weight=1)

    self.backButton = customtkinter.CTkButton(master=self.buttonFrame, text="Back", command=lambda: back(self, classInfo["id"], classInfo["name"]))
    self.backButton.grid(row=0, column=0, sticky="nsew", padx=10, pady=3)

    self.editButton = customtkinter.CTkButton(master=self.buttonFrame, text="Edit", command=lambda: classAddEdit(self, "edit", classInfo["name"]))
    self.editButton.grid(row=0, column=1, sticky="nsew", padx=10, pady=3)

def back(self, id, name):
    from screen.classroom import classroom

    classroom(self, id, name)
