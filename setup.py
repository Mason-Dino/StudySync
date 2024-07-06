import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("themes/teal.json")

class setup(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("400x240")
        self.columnconfigure((0,1,2), weight=1)
        self.rowconfigure(0, weight=1)

        self.side = customtkinter.CTkFrame(master=self)
        self.side.grid(row=0, column=0, padx=5, pady=5, sticky="nswe")

        self.main = customtkinter.CTkFrame(master=self)
        self.main.grid(row=0, column=1, columnspan=2, padx=5, pady=5, sticky="nswe")
        self.main.columnconfigure((0,1,2), weight=1)
        self.main.rowconfigure((0,1), weight=1)

        self.question = customtkinter.CTkLabel(master=self.main, text="What mode do you want?")
        self.question.grid(row=0, column=1, padx=5, pady=5)

        self.option = customtkinter.CTkOptionMenu(master=self.main, values=["Light", "Dark", "System"])
        self.option.grid(row=1, column=1, padx=5, pady=5)


    def button_function(self):
        print("button pressed")


if __name__ == "__main__":
    App = setup()
    App.mainloop()