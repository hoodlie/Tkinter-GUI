import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import sys
sys.path.append('..')

#from src.loadPages import Main as master

import utilities.utils as utls

class StartingPage(tk.Frame):

    def __init__(self, container, master):

        tk.Frame.__init__(self, container)

        tk.Label(self, text="Welcome to the program").grid(row=0, column=0)

        tk.Button(self, text="Login",
                  command=lambda: master.showPage(LoginPage)).grid(row=1, column=0)
        tk.Button(self, text="Register",
                  command=lambda: master.showPage(RegisterPage)).grid(row=1, column=1)
