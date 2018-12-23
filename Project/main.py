import os

import src.tkinter_load_pages as main
import utilities.utils as utls

cwd = os.path.dirname(os.path.realpath(__file__))

print("Current working directory:", cwd)


def reset_session():
    f = open("data\\items_in_cart.txt", "w")
    f.write("")
    f.close()


reset_session()

root = main.Main()
root.resizable(False, False)
root.configure(background="white")
# root.protocol("WM_DELETE_WINDOW", reset_session())
root.mainloop()

