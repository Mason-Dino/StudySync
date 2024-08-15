import customtkinter

def studyTimer(self):
    self.content = customtkinter.CTkFrame(master=self, corner_radius=6)
    self.content.grid(row=0, column=1, rowspan=3, columnspan=2, sticky="nsew", padx=10, pady=10)
    self.content.grid_columnconfigure(0, weight=1)

    self.header = customtkinter.CTkFrame(master=self.content, corner_radius=6, fg_color="transparent")
    self.header.grid(row=0, column=0, sticky="nsew", pady=20, padx=10)
    self.header.grid_columnconfigure(0, weight=1)

    self.timeLabel = customtkinter.CTkLabel(master=self.header, text="00:00:00", font=customtkinter.CTkFont(size=30, weight="bold"))
    self.timeLabel.grid(row=0, column=0, sticky="nsew")

    self.timeInput = customtkinter.CTkFrame(master=self.content, fg_color="transparent")
    self.timeInput.grid(row=1, column=0, sticky="nsew")
    self.timeInput.grid_columnconfigure((0, 1, 2), weight=1)

    self.hour = customtkinter.CTkEntry(master=self.timeInput, placeholder_text="Hour", font=customtkinter.CTkFont(size=15))
    self.hour.grid(row=0, column=0, sticky="nsew", pady=10, padx=10)

    self.minute = customtkinter.CTkEntry(master=self.timeInput, placeholder_text="Minute", font=customtkinter.CTkFont(size=15))
    self.minute.grid(row=0, column=1, sticky="nsew", pady=10, padx=10)

    self.second = customtkinter.CTkEntry(master=self.timeInput, placeholder_text="Second", font=customtkinter.CTkFont(size=15))
    self.second.grid(row=0, column=2, sticky="nsew", pady=10, padx=10)