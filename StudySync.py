from setup import setup
import customtkinter
import json

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green


class StudySync(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("700x400")
        self.title("StudySync")

        with open("setup.json", "r") as f:
            self.setupDir = json.load(f)

        self.numClasses = self.setupDir["numClasses"]
        print(self.numClasses)

        self.grid_columnconfigure((1,2), weight=1)
        self.grid_columnconfigure((3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.side = customtkinter.CTkFrame(master=self, corner_radius=0)  # Create the side frame
        self.side.grid(row=0, rowspan=3, column=0, sticky="nswe")  # Position the side frame

        self.name = customtkinter.CTkLabel(master=self.side, text="StudySync", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.name.grid(row=0, column=0, padx=15, pady=20)

        self.classes = customtkinter.CTkScrollableFrame(master=self.side)
        self.classes.grid(row=1, rowspan=2, column=0, sticky="nswe", padx=15, pady=10)

        for i in range(self.numClasses):
            self.button = customtkinter.CTkButton(master=self.classes, text="Class " + str(i + 1), command=self.button_function)
            self.button.grid(row=i + 1, padx=15, pady=10)

        self.settingsButton = customtkinter.CTkButton(master=self.side, text="Settings", command=self.settings)
        self.settingsButton.grid(row=3, column=0, padx=15, pady=5)



    def button_function(self):
        print("button pressed")

    def settings(self):
        print("selection cleared")


if __name__ == "__main__":
    with open("setup.json", "r") as f:
        setupDir = json.load(f)

    try:
        if setupDir["setupComplete"] == False or setupDir["setupComplete"] == None:
            app = setup()
            app.mainloop()

        if setupDir["setupComplete"] == True:
            app = StudySync()
            app.mainloop()

    except KeyError:
        app = setup()
        app.mainloop()