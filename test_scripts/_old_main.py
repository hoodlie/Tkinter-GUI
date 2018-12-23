import sys, os

cwd = os.path.dirname(os.path.realpath(__file__))

print("Current working directory:", cwd)

import src.tkinter_load_pages as main

#from register_page import RegisterPage
#from login_page import LoginPage

##class Main(tk.Tk):
##
##    def __init__(self, *args, **kwargs):
##        tk.Tk.__init__(self, *args, **kwargs)
##
##        #Setting things
##        self.geometry("300x150")
##        self.title("Main Page")
##
##        #Initializing container frame where all pages displayed
##        container = tk.Frame(self)
##        #Creating the container
##        container.pack(fill="both", expand=True)
##        container.grid_rowconfigure(0, weight=1)
##        container.grid_columnconfigure(0, weight=1)
##
##        #Creating dictionary to hold all pages
##        self.pages = {}
##
##        #Existing pages
##        currentPages = (LoginPage, RegisterPage, StartingPage)
##
##        print("-" * 15)
##        print("Beginning Init")
##        print("-" * 15)
##
##        #Loading each page
##        for pageSignature in (currentPages):
##            #pageSignatureName = pageSignature.__name__
##            #Initializing the page
##            pageSignatureLoaded = pageSignature(container, self)
##            print("DEBUG:", pageSignature(container, self))
##            #Creating a dictionary entry for page
##            self.pages[pageSignature] = pageSignatureLoaded
##            #Draw the pages
##            pageSignatureLoaded.grid(row=0, column=0, sticky="nsew")
##
##        print("-" * 15)
##        print("Ended Init")
##        print("-" * 15)
##        print(self.pages)
##
##        self.showPage(StartingPage)
##
##    def showPage(self, page):
##        print("From showPage():", page)
##        self.title(page.__name__)
##        pageToRaise = self.pages[page]
##        pageToRaise.tkraise()
##
## class RegisterPage(tk.Frame):
##
##    def __init__(self, container, master):
##
##        tk.Frame.__init__(self, container)
##
##        self.username = tk.StringVar()
##        self.password = tk.StringVar()
##
##        self.usernameLabel = tk.Label(self, text="Enter username:")
##        self.usernameEntry = tk.Entry(self, textvariable=self.username)
##
##        self.passwordLabel = tk.Label(self, text="Enter password:")
##        self.passwordEntry = tk.Entry(self, textvariable=self.password,
##                                      show="*")
##
##        self.submitButton = tk.Button(self, text="Register",
##        command=self.register_btn_pressed)
##
##        self.returnButton = tk.Button(self, text="Back to main page",
##        command=lambda: master.showPage(StartingPage))
##
##
##        self.usernameLabel.grid(row=0, column=0)
##        self.usernameEntry.grid(row=0, column=1)
##        self.passwordLabel.grid(row=1, column=0)
##        self.passwordEntry.grid(row=1, column=1)
##        self.submitButton.grid(row=2, column=0)
##        self.returnButton.grid(row=2, column=1)
##
##
##    def register_btn_pressed(self):
##
##        usernameTaken = False
##
##        self.w_username = self.username.get()
##        self.w_password = self.password.get()
##
##        if self.w_username == "" or self.w_password == "":
##            messagebox.showinfo("Nothing entered",
##                                "You have to enter something!")
##            return
##
##        data = utls.readFile("utilities\\userdata.txt")
##
##        for temp in data:
##
##            if self.w_username == temp.split(",")[0]:
##                messagebox.showinfo("Username taken",
##                                    "This username already exists!")
##                usernameTaken = True
##                break
##
##        if not usernameTaken:
##            utls.writeFile("utilities\\userdata.txt",
##                           f"{self.w_username}, {self.w_password}")
##
##        print(data)
##
##class LoginPage(tk.Frame):
##
##    def __init__(self, container, master):
##
##        tk.Frame.__init__(self, container)
##
##        self.username = tk.StringVar()
##        self.password = tk.StringVar()
##
##        self.usernameLabel = tk.Label(self, text="Enter username:")
##        self.usernameEntry = tk.Entry(self, textvariable=self.username)
##
##        self.passwordLabel = tk.Label(self, text="Enter password:")
##        self.passwordEntry = tk.Entry(self, textvariable=self.password,
##                                      show="*")
##
##        self.submitButton = tk.Button(self, text="Log in",
##        command=self.login_btn_pressed)
##        self.returnButton = tk.Button(self, text="Back to main page",
##        command=lambda: master.showPage(StartingPage))
##
##        self.usernameLabel.grid(row=0, column=0)
##        self.usernameEntry.grid(row=0, column=1)
##        self.passwordLabel.grid(row=1, column=0)
##        self.passwordEntry.grid(row=1, column=1)
##        self.submitButton.grid(row=2, column=0)
##        self.returnButton.grid(row=2, column=1)
##
##    def login_btn_pressed(self):
##
##        loggedIn = False
##
##        self.w_username = self.username.get()
##        self.w_password = self.password.get()
##
##        data = utls.readFile("utilities\\userdata.txt")
##
##        for temp in data:
##            c_username, c_password = temp.split(",")
##            c_password.strip()
##
##            print(self.w_password == c_password)
##            print(self.w_password, c_password)
##
##            #There's a " " before c_password and strip() doesn't work
##
##            if self.w_username == c_username and " " + self.w_password == c_password:
##                print("You're logged in!")
##                loggedIn = True
##                break
##
##
##        if not loggedIn:
##            messagebox.showinfo("Login Failed",
##                                "Wrong username or password")
##
##        print(data)
##
##class StartingPage(tk.Frame):
##
##    def __init__(self, container, master):
##
##        tk.Frame.__init__(self, container)
##
##        tk.Label(self, text="Welcome to the program").grid(row=0, column=0)
##
##        tk.Button(self, text="Login",
##        command=lambda: master.showPage(LoginPage)).grid(row=1, column=0)
##        tk.Button(self, text="Register",
##        command=lambda: master.showPage(RegisterPage)).grid(row=1, column=1)
##

root = main.Main()
root.mainloop()
