import customtkinter

def classAddEdit(self):
    self.content = customtkinter.CTkFrame(master=self, corner_radius=6)
    self.content.grid(row=0, column=1, rowspan=3, columnspan=2, sticky="nsew", padx=10, pady=10)

    self.test = customtkinter.CTkLabel(master=self.content, text="Class Add/Edit")
    self.test.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)