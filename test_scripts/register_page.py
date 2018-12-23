import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import sys
sys.path.append('..')

#from src.loadPages import Main as master

import utilities.utils as utls

class RegisterPage(tk.Frame):

    def __init__(self, container, master):

        tk.Frame.__init__(self, container)

        self.username = tk.StringVar()
        self.password = tk.StringVar()

        self.usernameLabel = tk.Label(self, text="Enter username:")
        self.usernameEntry = tk.Entry(self, textvariable=self.username)

        self.passwordLabel = tk.Label(self, text="Enter password:")
        self.passwordEntry = tk.Entry(self, textvariable=self.password,
                                      show="*")

        self.submitButton = tk.Button(self, text="Register",
        command=self.register_btn_pressed)

        self.returnButton = tk.Button(self, text="Back to main page",
        command=lambda: master.showPage(StartingPage))


        self.usernameLabel.grid(row=0, column=0)
        self.usernameEntry.grid(row=0, column=1)
        self.passwordLabel.grid(row=1, column=0)
        self.passwordEntry.grid(row=1, column=1)
        self.submitButton.grid(row=2, column=0)
        self.returnButton.grid(row=2, column=1)


    def register_btn_pressed(self):

        usernameTaken = False

        self.w_username = self.username.get()
        self.w_password = self.password.get()

        if self.w_username == "" or self.w_password == "":
            messagebox.showinfo("Nothing entered",
                                "You have to enter something!")
            return

        data = utls.read_file("utilities\\user_data.txt")

        for temp in data:

            if self.w_username == temp.split(",")[0]:
                messagebox.showinfo("Username taken",
                                    "This username already exists!")
                usernameTaken = True
                break

        if not usernameTaken:
            utls.write_file("utilities\\user_data.txt",
                           f"{self.w_username}, {self.w_password}")

        print(data)
