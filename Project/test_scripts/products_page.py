import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import utilities.utils as utls

class ProductsPage(tk.Frame):

    def __init__(self, container, master):
        tk.Frame.__init__(self, container)

        data = utls.read_file("data\\stocks.txt")

        print(data)

        tk.Label(self, text="Welcome to the products page!").grid(row=0, column=0)
        tk.Button(self, text="Go back!!!", command=lambda: master.show_page(StartingPage)).grid(row=0, column=1)