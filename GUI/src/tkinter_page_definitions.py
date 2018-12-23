import utilities.utils as utls

import tkinter as tk
# from tkinter import ttk
from tkinter import messagebox


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

        self.submitButton = tk.Button(self, text="Log in",
                                      command=lambda: self.login_btn_pressed(master))
        self.returnButton = tk.Button(self, text="Back to main page",
                                      command=lambda: master.show_page(StartingPage))

        self.usernameLabel.grid(row=0, column=0)
        self.usernameEntry.grid(row=0, column=1)
        self.passwordLabel.grid(row=1, column=0)
        self.passwordEntry.grid(row=1, column=1)
        self.submitButton.grid(row=2, column=0, pady=5)
        self.returnButton.grid(row=2, column=1, pady=5)

    def login_btn_pressed(self, master):

        logged_in = False

        w_username = self.username.get()
        w_password = self.password.get()

        data = utls.read_file("data\\user_data.txt")

        for temp in data:
            c_username, c_password = temp.split(",")
            c_password.strip()

            ##            print(self.w_password == c_password)
            ##            print(self.w_password, c_password)

            # There's a " " before c_password and strip() doesn't work

            if w_username == c_username and " " + w_password == c_password:
                print("You're logged in!")
                logged_in = True
                break

        print(data)

        if logged_in:
            master.show_page(ProductsPage)

        if not logged_in:
            messagebox.showinfo("Login Failed",
                                "Wrong username or password")


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
                                      command=lambda: self.register_btn_pressed(master))

        self.returnButton = tk.Button(self, text="Back to main page",
                                      command=lambda: master.show_page(StartingPage))

        self.usernameLabel.grid(row=0, column=0)
        self.usernameEntry.grid(row=0, column=1)
        self.passwordLabel.grid(row=1, column=0)
        self.passwordEntry.grid(row=1, column=1)
        self.submitButton.grid(row=2, column=0, pady=5)
        self.returnButton.grid(row=2, column=1, pady=5)

    def register_btn_pressed(self, master):

        username_taken = False

        w_username = self.username.get()
        w_password = self.password.get()

        if w_username == "" or w_password == "":
            messagebox.showinfo("Nothing entered",
                                "You have to enter something!")
            return

        data = utls.read_file("data\\user_data.txt")

        for temp in data:

            if w_username == temp.split(",")[0]:
                messagebox.showinfo("Username taken",
                                    "This username already exists!")
                username_taken = True
                break

        if not username_taken:
            utls.write_file("data\\user_data.txt",
                            f"{w_username}, {w_password}")
            messagebox.showinfo("Successful Login", "You've successfully logged in, returning to starting page!")
            master.show_page(StartingPage)

        print(utls.read_file("data\\user_data.txt"))


class StartingPage(tk.Frame):

    def __init__(self, container, master):
        tk.Frame.__init__(self, container)

        tk.Label(self, text="Welcome").grid(row=0, column=0)

        tk.Button(self, text="Login",
                  command=lambda: master.show_page(LoginPage)).grid(row=1, column=0)
        tk.Button(self, text="Register",
                  command=lambda: master.show_page(RegisterPage)).grid(row=1, column=1)


class ProductsPage(tk.Frame):
    offset_x, offset_y = 200, 20
    curr_offset_y = 70
    screen_x, screen_y = 600, 450

    def __init__(self, container, master):
        tk.Frame.__init__(self, container)

        data = utls.read_file("data\\stocks.txt")
        data = data[1:]

        print("Current stock:", data)

        tk.Label(self, text="Welcome to the products page!").place(x=200, y=0, width=180
                                                                   , height=20)

        tk.Label(self, text="Product name").place(x=20, y=50, width=200, height=20)
        tk.Label(self, text="In stock").place(x=220, y=50, width=200, height=20)
        tk.Label(self, text="Product price").place(x=420, y=50, width=200, height=20)

        for i in data:

            print("These are the current stocks:", i)

            product_name, product_in_stock, product_price = i.split(",")

            print(product_name, product_in_stock, product_price)

            tk.Button(self, text=product_name).place(x=20, y=self.curr_offset_y + self.offset_y,
                                                     width=200, height=20)
            tk.Label(self, text=product_in_stock).place(x=220, y=self.curr_offset_y + self.offset_y,
                                                        width=200, height=20)
            tk.Label(self, text=product_price).place(x=420, y=self.curr_offset_y + self.offset_y,
                                                     width=200, height=20)
            self.curr_offset_y += 20

        tk.Button(self, text="Go back",
                  command=lambda: master.show_page(StartingPage)).place(x=self.screen_x-100,
                                                                        y=self.screen_y-50)
