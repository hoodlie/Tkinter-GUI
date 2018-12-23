import os

import src.tkinter_load_pages as main

cwd = os.path.dirname(os.path.realpath(__file__))

print("Current working directory:", cwd)

root = main.Main()
root.resizable(False, False)
root.mainloop()

