import customtkinter
import json


def settings(self):
    self.content = customtkinter.CTkFrame(master=self)
    self.content.grid(row=0, column=1, rowspan=3, columnspan=2, sticky="nsew", padx=10, pady=10)

    self.content.grid_columnconfigure(0, weight=1)
    self.content.grid_rowconfigure(0, weight=1)

    self.test = customtkinter.CTkLabel(master=self.content, text="Settings")
    self.test.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    with open("setup.json", "r") as f:
        self.setupDir = json.load(f)

    self.appearance = customtkinter.CTkOptionMenu(master=self.content, values=["System", "Light", "Dark"], command=changeAppearanceMode, variable=customtkinter.StringVar(value=self.setupDir["mode"]))
    self.appearance.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

def changeAppearanceMode(new_appearance_mode: str):
    customtkinter.set_appearance_mode(new_appearance_mode)

    with open("setup.json", "r") as f:
        setupDir = json.load(f)

    setupDir["mode"] = new_appearance_mode
    with open("setup.json", "w") as f:
        json.dump(setupDir, f, indent=4)