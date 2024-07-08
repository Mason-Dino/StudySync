import customtkinter


def home(self):
    self.content = customtkinter.CTkFrame(master=self)
    self.content.grid(row=0, column=1, rowspan=3, columnspan=2, sticky="nsew", padx=10, pady=10)

    self.content.grid_columnconfigure(0, weight=1)
    self.content.grid_rowconfigure(0, weight=1)

    self.test = customtkinter.CTkLabel(master=self.content, text="Home")
    self.test.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)