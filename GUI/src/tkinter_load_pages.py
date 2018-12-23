import tkinter as tk

from src.tkinter_page_definitions import (LoginPage, RegisterPage, StartingPage, ProductsPage)


class Main(tk.Tk):
    currentPages = (LoginPage, RegisterPage, StartingPage, ProductsPage)
    RESOLUTION = "600x450"

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Setting things
        self.geometry(self.RESOLUTION)
        self.title("Main Page")

        # Initializing container frame where all pages displayed
        container = tk.Frame(self)
        # Creating the container
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=10)
        container.grid_columnconfigure(0, weight=10)

        # Creating dictionary to hold all pages
        self.pages = {}

        print("-" * 15)
        print("Beginning Init")
        print("-" * 15)

        # Loading each page
        for page_signature in self.currentPages:
            # page_signature_name = page_signature.__name__
            # Initializing the page
            page_signature_loaded = page_signature(container, self)
            print("DEBUG:", page_signature(container, self))
            # Creating a dictionary entry for page
            self.pages[page_signature] = page_signature_loaded
            # Draw the pages
            page_signature_loaded.grid(row=0, column=0, sticky="nsew")

        print("-" * 15)
        print("Ended Init")
        print("-" * 15)
        print(self.pages)

        self.show_page(StartingPage)

    def show_page(self, page):
        print("From showPage():", page)
        self.title(page.__name__)
        page_to_raise = self.pages[page]
        page_to_raise.tkraise()
