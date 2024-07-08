from setup import setup
import customtkinter
import json



class StudySync(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        with open("setup.json", "r") as f:
            self.setupDir = json.load(f)

        self.geometry("700x400")
        self.title("StudySync")


        customtkinter.set_appearance_mode(self.setupDir["mode"])  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme(f"themes/{self.setupDir['theme'].lower()}.json")  # Themes: blue (default), dark-blue, green


        self.numClasses = self.setupDir["numClasses"]
        print(self.numClasses)

        self.grid_columnconfigure((1,2), weight=1)
        self.grid_columnconfigure((3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.side = customtkinter.CTkFrame(master=self, corner_radius=0)  # Create the side frame
        self.side.grid(row=0, rowspan=3, column=0, sticky="nswe")  # Position the side frame

        self.name = customtkinter.CTkLabel(master=self.side, text="StudySync", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.name.grid(row=0, column=0, padx=15, pady=20)

        self.classes = customtkinter.CTkScrollableFrame(master=self.side, height=250, fg_color="gray17")
        self.classes.grid_columnconfigure(0, weight=1)
        self.classes.grid(row=1, rowspan=2, column=0, sticky="nswe", pady=10)
        self.classFunction = [self.class1, self.class2, self.class3, self.class4, self.class5, self.class6, self.class7, self.class8, self.class9, self.class10]
        for i in range(self.numClasses):
            self.button = customtkinter.CTkButton(master=self.classes, text=self.setupDir[f"class{i+1}"]["className"], command=self.classFunction[i])
            self.button.grid(row=i + 1, column=0, pady=10)

        self.settingsButton = customtkinter.CTkButton(master=self.side, text="Settings", command=self.settings)
        self.settingsButton.grid(row=3, column=0, padx=15, pady=5)



    def button_function(self):
        print("button pressed")

    def settings(self):
        print("selection cleared")

    def class1(self):
        print(self.setupDir["class1"]["className"])

    def class2(self):
        print(self.setupDir["class2"]["className"])      

    def class3(self):
        print(self.setupDir["class3"]["className"])

    def class4(self):
        print(self.setupDir["class4"]["className"])

    def class5(self):
        print(self.setupDir["class5"]["className"])

    def class6(self):
        print(self.setupDir["class6"]["className"])

    def class7(self):
        print(self.setupDir["class7"]["className"])

    def class8(self):
        print(self.setupDir["class8"]["className"])

    def class9(self):
        print(self.setupDir["class9"]["className"])

    def class10(self):
        print(self.setupDir["class10"]["className"])


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