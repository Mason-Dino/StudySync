from setup import setup
import customtkinter
import json

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green


class StudySync(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("400x240")

        self.button = customtkinter.CTkButton(master=self, text="Button 2", command=self.button_function)
        self.button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

    def button_function(self):
        print("button pressed")


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
    