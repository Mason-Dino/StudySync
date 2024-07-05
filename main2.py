import customtkinter
from main import Setup_App

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("400x240")

        self.button = customtkinter.CTkButton(master=self, text="Button 1", command=self.button_function)
        self.button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

    def button_function(self):
        print("button pressed")

        AppSetup = Setup_App()
        AppSetup.mainloop()


if __name__ == "__main__":
    app = App()
    app.mainloop()
