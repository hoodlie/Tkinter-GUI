# The code for changing pages was derived from: http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
# License: http://creativecommons.org/licenses/by-sa/3.0/	

import tkinter as tk
from tkinter import ttk

"""
Integrating my code into an existing working code taken from an open source application:
https://github.com/Sea-of-BTC/Bitcoin-Trading-Client
which was derived from: 
https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
"""

LARGE_FONT= ("Verdana", 12)


class Application(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "Sea of BTC Client")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, LoginPage, RegisterPage):

            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        print(self.frames)
        self.show_frame(StartPage)

    def show_frame(self, cont):
        print(cont)
        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        tk.Label(self, text="Welcome to the program").grid(row=0, column=0)
        tk.Button(self, text="Login",
        command=controller.show_frame(LoginPage)).grid(row=1, column=0)
        tk.Button(self, text="Register",
        command=controller.show_frame(RegisterPage)).grid(row=1, column=1)
    


class RegisterPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.username = tk.StringVar()
        self.password = tk.StringVar()

        self.usernameLabel = tk.Label(self, text="Enter username:")
        self.usernameEntry = tk.Entry(self, textvariable=self.username)

        self.passwordLabel = tk.Label(self, text="Enter password:")
        self.passwordEntry = tk.Entry(self, textvariable=self.password,
                                      show="*")

        self.submitButton = tk.Button(self, text="Register",
        command=self.register_btn_pressed)

        try:
            self.returnButton = tk.Button(self, text="Back to main page",
            command=controller.showPage(StartingPage))
        except:
            pass

        self.usernameLabel.grid(row=0, column=0)
        self.usernameEntry.grid(row=0, column=1)
        self.passwordLabel.grid(row=1, column=0)
        self.passwordEntry.grid(row=1, column=1)
        try:
            self.submitButton.grid(row=2, column=0)
        except:
            pass


    def register_btn_pressed(self):

        usernameTaken = False

        self.w_username = self.username.get()
        self.w_password = self.password.get()

        data = utls.readFile("userdata.txt")

        for temp in data:

            if self.w_username == temp.split(",")[0]:
                messagebox.showinfo("Username taken",
                                    "This username already exists!")
                usernameTaken = True
                break

        if not usernameTaken:
            utls.writeFile("userdata.txt",
                           f"{self.w_username}, {self.w_password}")

        print(data)


class LoginPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.username = tk.StringVar()
        self.password = tk.StringVar()

        self.usernameLabel = tk.Label(self, text="Enter username:")
        self.usernameEntry = tk.Entry(self, textvariable=self.username)

        self.passwordLabel = tk.Label(self, text="Enter password:")
        self.passwordEntry = tk.Entry(self, textvariable=self.password,
                                      show="*")
        
        try:
            self.submitButton = tk.Button(self, text="Log in",
            command=self.login_btn_pressed)
            self.returnButton = tk.Button(self, text="Back to main page",
            command=controller.showPage(StartingPage))
        except:
            pass

        self.usernameLabel.grid(row=0, column=0)
        self.usernameEntry.grid(row=0, column=1)
        self.passwordLabel.grid(row=1, column=0)
        self.passwordEntry.grid(row=1, column=1)
        self.submitButton.grid(row=2, column=0)
        try:
            self.returnButton.grid(row=2, column=1)
        except:
            pass

    def login_btn_pressed(self):

        loggedIn = False

        self.w_username = self.username.get()
        self.w_password = self.password.get()

        data = utls.readFile("userdata.txt")

        for temp in data:
            c_username, c_password = temp.split(",")
            c_password.strip()

##            print(self.w_password == c_password)
##            print(self.w_password, c_password)

            #There's a " " before c_password and strip() doesn't work

            if self.w_username == c_username and " " + self.w_password == c_password:
                print("You're logged in!")
                loggedIn = True
                break


        if not loggedIn:
            messagebox.showinfo("Login Failed",
                                "Wrong username or password")

        print(data)


app = SeaofBTCapp()
app.mainloop()
