import customtkinter
from task import *

def showAssignment(self, id):
    self.content = customtkinter.CTkFrame(master=self, corner_radius=6)
    self.content.grid(row=0, column=1, rowspan=3, columnspan=2, sticky="nsew", padx=10, pady=10)
    self.content.grid_columnconfigure((0, 1), weight=1)

    self.title = customtkinter.CTkLabel(master=self.content, text="Assignment", font=customtkinter.CTkFont(size=20, weight="bold"))

    classInfo = getMainTaskSingle(id)

    print(classInfo)

