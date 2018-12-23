import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import utilities.utils as utls


class LoginPage(tk.Frame):

    def __init__(self, container, master):

        tk.Frame.__init__(self, container)

        self.username = tk.StringVar()
        self.password = tk.StringVar()

        self.usernameLabel = tk.Label(self, text="Enter username:")
        self.usernameEntry = tk.Entry(self, textvariable=self.username)

        self.passwordLabel = tk.Label(self, text="Enter password:")
        self.passwordEntry = tk.Entry(self, textvariable=self.password,
                                      show="*")

        self.submitButton = ttk.Button(self, text="Log in",
                                       command=self.login_btn_pressed)
        self.returnButton = ttk.Button(self, text="Back to main page",
                                       command=lambda: master.showPage(StartingPage))

        self.usernameLabel.grid(row=0, column=0)
        self.usernameEntry.grid(row=0, column=1)
        self.passwordLabel.grid(row=1, column=0)
        self.passwordEntry.grid(row=1, column=1)
        self.submitButton.grid(row=2, column=0)
        self.returnButton.grid(row=2, column=1)

    def login_btn_pressed(self):

        loggedIn = False

        self.w_username = self.username.get()
        self.w_password = self.password.get()

        data = utls.read_file("utilities\\user_data.txt")

        for temp in data:
            c_username, c_password = temp.split(",")
            c_password.strip()

            ##            print(self.w_password == c_password)
            ##            print(self.w_password, c_password)

            # There's a " " before c_password and strip() doesn't work

            if self.w_username == c_username and " " + self.w_password == c_password:
                print("You're logged in!")
                loggedIn = True
                break

        if not loggedIn:
            messagebox.showinfo("Login Failed",
                                "Wrong username or password")

        print(data)
