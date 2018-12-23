import utilities.utils as utls

import tkinter as tk
# from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog


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
                                      command=lambda: master.show_page(StartingPage) and master.refresh_page(LoginPage))

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
            master.refresh_page(LoginPage)
            master.show_page(MenuPage)

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
                                      command=lambda: master.show_page(StartingPage) and master.refresh_page(
                                          RegisterPage))

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
                            f"{w_username}, {w_password}", "a")
            messagebox.showinfo("Successful Login", "You've successfully logged in, returning to starting page!")
            master.refresh_page(RegisterPage)
            master.show_page(StartingPage)

        print(utls.read_file("data\\user_data.txt"))


class StartingPage(tk.Frame):

    def __init__(self, container, master):
        tk.Frame.__init__(self, container)

        tk.Label(self, text="Welcome").grid(row=0, column=0)

        tk.Button(self, text="Login",
                  command=lambda: master.show_page(LoginPage) and master.refresh_page(StartingPage)).grid(row=1,
                                                                                                          column=0)
        tk.Button(self, text="Register",
                  command=lambda: master.show_page(RegisterPage) and master.refresh_page(StartingPage)).grid(row=1,
                                                                                                             column=1)


class ProductsPage(tk.Frame):
    offset_x, offset_y = 200, 20
    curr_offset_y = 70
    screen_x, screen_y = 800, 450

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

        self.buttons = dict()

        for i in data:
            print("These are the current stocks:", i)

            product_name, product_in_stock, product_price, desc = i.split(",")

            print(product_name, product_in_stock, product_price)

            temp = tk.Button(self, text=product_name,
                             command=lambda c=i: self.generate_item_page(master, c))

            temp.place(x=20, y=self.curr_offset_y + self.offset_y, width=200, height=20)

            tk.Label(self, text=product_in_stock).place(x=220, y=self.curr_offset_y + self.offset_y,
                                                        width=200, height=20)
            tk.Label(self, text=product_price).place(x=420, y=self.curr_offset_y + self.offset_y,
                                                     width=200, height=20)
            self.curr_offset_y += 20

            print("BUTTON CREATED:", temp)

            self.buttons[temp] = [product_name, product_in_stock, product_price, desc]

            print(self.buttons)

        tk.Button(self, text="Go back",
                  command=lambda: (master.show_page(MenuPage)
                                   and master.refresh_page(ProductsPage))).place(x=self.screen_x - 100,
                                                                                 y=self.screen_y - 50)
        tk.Button(self, text="Cart",
                  command=lambda:master.show_page(CartPage)).place(x=100, y=400, width=100)

    def generate_item_page(self, master, item_to_display):
        print("TO DISPLAY:", item_to_display)

        ModelPage.name = item_to_display.split(",")[0]
        ModelPage.amount = item_to_display.split(",")[1]
        ModelPage.price = item_to_display.split(",")[2]
        ModelPage.desc = item_to_display.split(",")[3]

        print(ModelPage.desc)

        master.refresh_page(ModelPage)
        master.show_page(ModelPage)


class MenuPage(tk.Frame):

    def __init__(self, container, master):
        tk.Frame.__init__(self, container)

        tk.Button(self, text="Buy stuff",
                  command=lambda: master.show_page(ProductsPage) and master.refresh_page(MenuPage)).grid(row=0,
                                                                                                         column=0)
        tk.Button(self, text="Supply stuff",
                  command=lambda: master.show_page(SupplyPage) and master.refresh_page(MenuPage)).grid(row=0, column=1)

        tk.Button(self, text="Go back",
                  command=lambda: master.show_page(StartingPage) and master.refresh_page(MenuPage)).grid(row=0,
                                                                                                         column=2)


class SupplyPage(tk.Frame):

    def __init__(self, container, master):

        tk.Frame.__init__(self, container)

        self.stock_amount = tk.StringVar()
        self.product_price = tk.StringVar()
        self.product_name = tk.StringVar()

        tk.Label(self, text="Product name:").grid(row=0, column=0)
        tk.Entry(self, textvariable=self.product_name).grid(row=0, column=1, sticky="w")

        tk.Label(self, text="Amount supplying:").grid(row=1, column=0)
        tk.Entry(self, textvariable=self.stock_amount).grid(row=1, column=1, sticky="w")

        tk.Label(self, text="Price per product:").grid(row=2, column=0)
        tk.Entry(self, textvariable=self.product_price).grid(row=2, column=1, sticky="w")

        tk.Label(self, text="Enter description:").grid(row=3, column=0)
        self.description = tk.Text(self, width=50, height=20)

        self.description.grid(row=3, column=1)

        tk.Button(self, text="Submit",
                  command=lambda: self.btn_pressed(master)).grid(row=4, column=0, padx=15, pady=15, sticky="w")
        tk.Button(self, text="Go back",
                  command=lambda: master.show_page(MenuPage) and master.refresh_page(ProductsPage)).grid(row=4,
                                                                                                         column=2,
                                                                                                         sticky="e")

    def btn_pressed(self, master):
        f = open("data\\stocks.txt")
        data = [line for line in f]
        f.close()

        c_product_name = self.product_name.get()
        c_product_price = self.product_price.get()
        c_stock_amount = self.stock_amount.get()
        c_description = self.description.get(1.0, tk.END).replace("\n", "")

        invalid = False

        print(c_product_name)
        print(c_stock_amount)
        print(c_product_price)
        print("Thsi is decec:", c_description)

        for temp in data:

            if c_product_name == temp.split(",")[0]:
                invalid = True
                messagebox.showinfo("Unable to submit product", "Product name already exists!")
                break

        if c_product_name == "":
            invalid = True
        if c_stock_amount == "":
            invalid = True
        if c_product_price == "":
            invalid = True
        if c_description == "":
            invalid = True

        if len(c_product_name) > 17:
            invalid = True
            messagebox.showinfo("Unable to submit product",
                                "Product name must be less than 16 symbols and at least 1 symbol")
        if len(c_description) < 5:
            invalid = True
            messagebox.showinfo("Unable to submit product", "Description must be at least 5 symbols")

        if len(c_stock_amount) > 10:
            invalid = True
            messagebox.showinfo("Unable to submit product", "Too much stock")

        if len(c_product_price) > 10:
            invalid = True
            messagebox.showinfo("Unable to submit product", "Too expensive")

        if invalid:
            messagebox.showinfo("Unable to submit product", "One of the fields is invalid!")

        if not invalid:
            print(f"Written: {c_product_name}, {c_stock_amount}, {c_product_price}, {c_description}")
            utls.write_file("data\\stocks.txt",
                            f"{c_product_name}, {c_stock_amount}, {c_product_price}, {c_description}", "b")

            messagebox.showinfo("Success!", "Successfully submitted product, returning back to menu")

            master.refresh_page(SupplyPage)
            master.refresh_page(ProductsPage)
            master.show_page(MenuPage)


class ModelPage(tk.Frame):

    name = ""
    amount = ""
    price = ""
    desc = ""

    def __init__(self, container, master):
        tk.Frame.__init__(self, container)

        tk.Label(self, text="Product name:").grid(row=0, column=0)
        tk.Label(self, text=self.name).grid(row=0, column=1)

        tk.Label(self, text="Product price:").grid(row=1, column=0)
        tk.Label(self, text=self.price).grid(row=1, column=1)

        tk.Label(self, text="In stock:").grid(row=2, column=0)
        tk.Label(self, text=self.amount).grid(row=2, column=1)

        tk.Label(self, text="Product description").grid(row=3, column=0)
        tk.Message(self, text=self.desc, width=300).grid(row=3, column=1, sticky="s")

        tk.Button(self, text="X",
                  command=lambda: self.delete_button_pressed(master)).place(x=525, y=10)

        tk.Button(self, text="+",
                  command=lambda: self.add_existing_stock(master)).place(x=525, y=50)

        tk.Button(self, text="Buy",
                  command=lambda: self.buy_button(master)).place(x=50, y=400)

        tk.Button(self, text="Back", command=lambda: master.show_page(ProductsPage)).place(x=600,
                                                                                           y=400)

    def delete_button_pressed(self, master):

        data = utls.read_file("data\\stocks.txt")

        for index in range(len(data)):

            print(index)
            print(data[index])

            c_name = data[index].split(",")[0]

            if self.name == c_name:
                print(f"Deleting stock {data[index]}")
                del data[index]
                break

        f = open("data\\stocks.txt", "w")

        for temp in data:
            if data.index(temp) != 0:
                f.write("\n")
            f.write(temp)

        f.close()

        messagebox.showinfo("Deleted stock", f"{self.name} has been deleted")

        master.refresh_page(ProductsPage)

    def buy_button(self, master):
        invalid = False

        amount = simpledialog.askstring("Buying item", "Enter amount you want to buy: ")

        print("COMPARING PRICES:", int(amount), int(self.amount))

        if int(amount) > int(self.amount) or int(amount) < 0:
            invalid = True
            messagebox.showinfo("Invalid amount", "You entered an invalid amount")

        if not invalid:
            utls.write_file("data\\items_in_cart.txt",
                            f"{self.name}, {amount}, {self.price}")

        master.refresh_page(CartPage)

    def add_existing_stock(self, master):

        amount = simpledialog.askstring("Refilling stock", "Enter amount you want to add: ")

        data = utls.read_file("data\\stocks.txt")

        print("DATA:", data)

        for index in range(len(data)):

            temp_name = data[index].split(",")[0]
            amount_to_fill = str(int(amount) + int(data[index].split(",")[1]))

            if self.name == temp_name:

                data[index] = f"{data[index].split(',')[0]}," \
                    f"{amount_to_fill}," \
                    f"{data[index].split(',')[2]}," \
                    f"{data[index].split(',')[3]}"

        print("NEW DATA:", data)

        f = open("data\\stocks.txt", "w")

        for temp in data:
            print(temp)
            if data.index(temp) != 0:
                f.write("\n")
            f.write(temp)

        f.close()

        messagebox.showinfo("Refill successful", "Successfully refilled stock")

        master.refresh_page(ProductsPage)
        # master.show_page(ProductsPage)


class CartPage(tk.Frame):
    offset_x, offset_y = 200, 20
    curr_offset_y = 70
    screen_x, screen_y = 800, 450

    def __init__(self, container, master):

        tk.Frame.__init__(self, container)

        data = utls.read_file("data\\items_in_cart.txt")

        tk.Label(self, text="Welcome to the products page!").place(x=200, y=0, width=180
                                                                   , height=20)

        tk.Label(self, text="Product name").place(x=20, y=50, width=200, height=20)
        tk.Label(self, text="Bought").place(x=220, y=50, width=200, height=20)
        tk.Label(self, text="Product price").place(x=420, y=50, width=200, height=20)
        tk.Label(self, text="Total").place(x=620, y=50, width=200, height=20)

        self.buttons = dict()
        total = 0

        for i in data:
            print("These are the current stocks:", i)

            product_name, product_amount, product_price = i.split(",")

            print(product_name, product_amount, product_price)

            tk.Label(self, text=product_name).place(x=20, y=self.curr_offset_y + self.offset_y,
                                                    width=200, height=20)
            tk.Label(self, text=product_amount).place(x=220, y=self.curr_offset_y + self.offset_y,
                                                      width=200, height=20)
            tk.Label(self, text=product_price).place(x=420, y=self.curr_offset_y + self.offset_y,
                                                     width=200, height=20)
            tk.Label(self, text=str(float(product_price.strip())*float(product_amount.strip()))).place(x=620,
                                                                                                   y=(self.curr_offset_y +
                                                                                                      self.offset_y),
                                                                                                   width=200, height=20)
            total += float(product_price.strip())*float(product_amount.strip())

            self.curr_offset_y += 20
        tk.Label(self, text=str(total)).place(x=620,
                                              y=(self.curr_offset_y + self.offset_y),
                                              width=200, height=20)

        tk.Button(self, text="Go back",
                  command=lambda: (master.show_page(ProductsPage)
                                   and master.refresh_page(CartPage))).place(x=self.screen_x - 100,
                                                                             y=self.screen_y - 50)
        tk.Button(self, text="Checkout", command=lambda: self.checkout(master)).place(x=100, y=400)

    def checkout(self, master):

        stocks_to_update = utls.read_file("data\\stocks.txt")
        stocks_in_cart = utls.read_file("data\\items_in_cart.txt")

        print("OLD:", stocks_to_update)

        for stocks in stocks_in_cart:

            stock_name = stocks.split(",")[0]
            stock_amount = stocks.split(",")[1]

            for index in range(len(stocks_to_update)):

                stock_to_update_name = stocks_to_update[index].split(",")[0]
                stock_to_update_amount = stocks_to_update[index].split(",")[1]

                if stock_to_update_name == stock_name:
                    print("AAA:", stock_to_update_amount)
                    stock_to_update_amount = float(stock_to_update_amount) - float(stock_amount)
                    print(stock_to_update_amount)
                    stock_to_update_amount = int(stock_to_update_amount)

                    stocks_to_update[index] = f"{stocks_to_update[index].split(',')[0]}, " \
                        f"{stock_to_update_amount}, " \
                        f"{stocks_to_update[index].split(',')[2]}, " \
                        f"{stocks_to_update[index].split(',')[3]}"

        print("NEW:", stocks_to_update)

        f = open("data\\stocks.txt", "w")

        for temp in stocks_to_update:
            if stocks_to_update.index(temp) != 0:
                f.write("\n")
            f.write(temp)

        f.close()

        f = open("data\\items_in_cart.txt", "w")

        f.write("")

        f.close()

        master.refresh_page(ProductsPage)



