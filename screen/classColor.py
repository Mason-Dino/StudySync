import customtkinter
import json

from themes.theme import loadColor

def showClassColors(self):
    self.content = customtkinter.CTkScrollableFrame(master=self)
    self.content.grid(row=0, column=1, rowspan=3, columnspan=2, sticky="nsew", padx=10, pady=10)
    self.content.grid_columnconfigure((0,1), weight=1)

    with open("setup.json", "r") as f:
        self.setupDir = json.load(f)

    numClasses = self.setupDir["numClasses"]

    for i in range(numClasses):
        self.className = customtkinter.CTkLabel(master=self.content, text=f"{self.setupDir[f'class{i+1}']['name']}:", font=customtkinter.CTkFont(size=15))
        self.className.grid(row=i, column=0, sticky="nsew", padx=10, pady=10)

        self.color = customtkinter.CTkFrame(master=self.content, fg_color=loadColor(self.setupDir[f"class{i+1}"]["color"]), height=20)
        self.color.grid(row=i, column=1, sticky="nsew", padx=10, pady=10)
