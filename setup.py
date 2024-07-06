import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("themes/teal.json")

class setup(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("400x240")
        self.columnconfigure((0,1,2), weight=1)
        self.rowconfigure(0, weight=1)

        self.side = customtkinter.CTkFrame(master=self, width=75, corner_radius=0)
        self.side.grid(row=0, column=0, sticky="nswe")
        self.side.columnconfigure(0, weight=1)
        self.side.rowconfigure((0,1), weight=1)

        self.logo = customtkinter.CTkLabel(master=self.side, anchor="n", text="Setup", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo.grid(row=0, column=0, padx=5, pady=5)

        self.main = customtkinter.CTkFrame(master=self)
        self.main.grid(row=0, column=1, columnspan=2, padx=10, pady=5, sticky="nswe")
        self.main.columnconfigure((0,1,2), weight=1)
        self.main.rowconfigure((0,1), weight=1)

        self.questionFrame1 = customtkinter.CTkFrame(master=self.main)
        self.questionFrame1.grid(row=0, column=1, padx=5, pady=5, sticky="nswe")
        self.questionFrame1.columnconfigure(0, weight=1)
        self.questionFrame1.rowconfigure((0,1), weight=1)

        self.question = customtkinter.CTkLabel(master=self.questionFrame1, text="What mode do you want?")
        self.question.grid(row=0, column=0, padx=5, pady=5)

        self.option = customtkinter.CTkOptionMenu(master=self.questionFrame1, values=["Light", "Dark", "System"])
        self.option.grid(row=1, column=0, padx=5, pady=5)


        self.pageNum = 1
        self.nextlast = customtkinter.CTkSegmentedButton(master=self.main, values=["Last", "Next"], command=self.pageFunction)
        self.nextlast.grid(row=2, column=1, padx=5, pady=5)


    def pageFunction(self, value):
        self.nextlast.set(None)

        if value == "Last" and self.pageNum == 1:
            pass

        elif value == "Next":
            self.pageNum += 1

        elif value == "Last":
            self.pageNum -= 1

        print(self.pageNum)


if __name__ == "__main__":
    App = setup()
    App.mainloop()