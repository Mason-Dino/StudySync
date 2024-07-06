import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("themes/teal.json")

class setup(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("400x240")
        self.columnconfigure((0,1,2), weight=1)
        self.rowconfigure((0,1), weight=1)

        self.side = customtkinter.CTkFrame(master=self, width=75, corner_radius=0)
        self.side.grid(row=0, rowspan=3, column=0, sticky="nswe")
        self.side.columnconfigure(0, weight=1)
        self.side.rowconfigure((0,1), weight=1)

        self.logo = customtkinter.CTkLabel(master=self.side, anchor="n", text="Setup", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo.grid(row=0, column=0, padx=5, pady=5)

        self.questionFrame1 = customtkinter.CTkFrame(master=self)
        self.questionFrame1.grid(row=0, column=1, columnspan=3, rowspan=2, padx=5, pady=5, sticky="nswe")
        self.questionFrame1.columnconfigure(0, weight=1)
        self.questionFrame1.rowconfigure((0,1), weight=1)

        self.question = customtkinter.CTkLabel(master=self.questionFrame1, text="What mode do you want?")
        self.question.grid(row=0, column=0, padx=5, pady=5)

        self.mode = customtkinter.CTkOptionMenu(master=self.questionFrame1, values=["Light", "Dark", "System"])
        self.mode.grid(row=1, column=0, padx=5, pady=5)

        self.questionFrame2 = customtkinter.CTkFrame(master=self)
        self.questionFrame2.columnconfigure(0, weight=1)
        self.questionFrame2.rowconfigure((0,1), weight=1)

        self.question = customtkinter.CTkLabel(master=self.questionFrame2, text="What theme do you want?")
        self.question.grid(row=0, column=0, padx=5, pady=5)

        self.theme = customtkinter.CTkOptionMenu(master=self.questionFrame2, values=["Purple", "Orange", "Teal", "Red", "Yellow", "Green", "Blue", "Grey"])
        self.theme.grid(row=1, column=0, padx=5, pady=5)


        self.pageNum = 1
        self.pageButton = customtkinter.CTkSegmentedButton(master=self, values=["Last", "Next"], command=self.page)
        self.pageButton.grid(row=2, column=1, columnspan=3, padx=5, pady=5, sticky="nswe")


    def page(self, value):
        self.pageButton.set(None)

        if value == "Last" and self.pageNum == 1:
            pass

        elif value == "Next":
            self.pageNum += 1

            if self.pageNum == 2:
                self.questionFrame1.destroy()
                self.questionFrame2.grid(row=0, column=1, columnspan=3, rowspan=2, padx=5, pady=5, sticky="nswe")

        elif value == "Last":
            self.pageNum -= 1

        print(self.pageNum)


if __name__ == "__main__":
    App = setup()
    App.mainloop()