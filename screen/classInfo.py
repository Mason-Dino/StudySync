import customtkinter

from task import getClassInfo

def classInfoScreen(self, id):
    classInfo = getClassInfo(id)

    self.content = customtkinter.CTkFrame(master=self)
    self.content.grid(row=0, column=1, rowspan=3, columnspan=2, sticky="nsew", padx=10, pady=10)