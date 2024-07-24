import customtkinter
import json

from themes.theme import topLevel

def classAddEdit(self, type: str, name: str = None):
    self.type = type

    self.content = customtkinter.CTkScrollableFrame(master=self, corner_radius=6)
    self.content.grid(row=0, column=1, rowspan=3, columnspan=2, sticky="nsew", padx=10, pady=10)
    self.content.grid_columnconfigure(0, weight=1)

    with open("setup.json", "r") as f:
        setupDir = json.load(f)

    self.className = customtkinter.CTkEntry(master=self.content, placeholder_text="Class Name")
    self.className.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

    self.cosmetics = customtkinter.CTkFrame(master=self.content, fg_color=topLevel())
    self.cosmetics.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)

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
