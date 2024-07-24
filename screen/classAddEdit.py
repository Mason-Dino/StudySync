import customtkinter
import json

from themes.theme import topLevel
from icon import getIcons

def classAddEdit(self, type: str, name: str = None):
    self.type = type

    self.content = customtkinter.CTkFrame(master=self, corner_radius=6)
    self.content.grid(row=0, column=1, rowspan=3, columnspan=2, sticky="nsew", padx=10, pady=10)
    self.content.grid_columnconfigure(0, weight=1)

    self.title = customtkinter.CTkLabel(master=self.content, text=f"Class {type.capitalize()}",
                                        font=customtkinter.CTkFont(size=20, weight="bold"))
    self.title.grid(row=0, column=0, pady=10)

    with open("setup.json", "r") as f:
        setupDir = json.load(f)
    
    self.classFrame = customtkinter.CTkFrame(master=self.content, fg_color=topLevel())
    self.classFrame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
    self.classFrame.grid_columnconfigure((0), weight=1)

    self.className = customtkinter.CTkEntry(master=self.classFrame, placeholder_text="Class Name")
    self.className.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

    self.cosmetics = customtkinter.CTkFrame(master=self.content, fg_color=topLevel())
    self.cosmetics.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)
    self.cosmetics.grid_columnconfigure((0,1), weight=1)

    self.subject = customtkinter.CTkOptionMenu(master=self.cosmetics, values=["Math", "Science", "English",  "History", "Social Studies", "World Language", "Fine Arts/Music", "Arts", "Physical Education", "Other"],
                                                variable=customtkinter.StringVar(value="Subject"))
    self.subject.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    self.icon = customtkinter.CTkOptionMenu(master=self.cosmetics, values=getIcons(), variable=customtkinter.StringVar(value="Icon"))
    self.icon.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

    self.color = customtkinter.CTkOptionMenu(master=self.cosmetics, values=["Teal", "Orange", "Purple", "Red", "Yellow", "Green", "Blue"],
                                                variable=customtkinter.StringVar(value="Color"))
    self.color.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

    self.teacherFrame = customtkinter.CTkFrame(master=self.content, fg_color=topLevel())
    self.teacherFrame.grid(row=3, column=0, sticky="nsew", padx=10, pady=10)
    self.teacherFrame.grid_columnconfigure((0,1), weight=1)

    self.teacher = customtkinter.CTkEntry(master=self.teacherFrame, placeholder_text="Teacher")
    self.teacher.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    self.email = customtkinter.CTkEntry(master=self.teacherFrame, placeholder_text="Email")
    self.email.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)



    if type == "add":
        numClass = setupDir["numClasses"]

    elif type == "edit":
        for i in range(setupDir["numClasses"]):
            if setupDir[f"class{i+1}"]["name"] == name:
                classNum = i + 1

        name = setupDir[f"class{classNum}"]["name"]
        subject = setupDir[f"class{classNum}"]["subject"]
        icon = setupDir[f"class{classNum}"]["icon"]
        color = setupDir[f"class{classNum}"]["color"]
        teacher = setupDir[f"class{classNum}"]["teacher"]
        email = setupDir[f"class{classNum}"]["email"]
