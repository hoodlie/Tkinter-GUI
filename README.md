<h1> GUI made in Tkinter and Python by me :) </h1>

<h2> Notes to reader </h2>

A fraction of my code is derived from https://pythonprogramming.net/tkinter-depth-tutorial-making-actual-program/ and http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter, however most of the code was made by me and only me :)
I used these resources for an introduction to tkinter and object oriented programming. 

<h1> Introduction to Project </h1>

<h2> Contents of project </h2>
<ul>
  <a href="#Starting page"><li>Starting page</li></a>
  <li>Login page</li>
  <li>Register page</li>
  <li>Product page</li>
  <li>Supplier page</li>
  <li>Cart page</li>
  <li>Starting page</li>
  <li>Menu page</li>
  <li>Model Item page</li>
<ul>

<h2 id="#Starting page"> Starting page </h2>
<img src="screenshots/starting_page">
<img src="screenshots/login_page">
<img src="screenshots/register_page">
<img src="screenshots/products_page">
<img src="screenshots/supplier_page">
<img src="screenshots/cart_page">
<img src="screenshots/menu_page">
<img src="screenshots/mode_page">

<h1> Changelog </h1>

Update 1.0 (22/12/2018)

- Created the application
- Created utils.py
- Created test scripts for login, register and starting pages
- Created user_data.txt
- Created main.py
- Created Main class which interconnects pages
- Integrated login, register, starting pages into main.py
- Added read and write to files to register/login

Update 1.1 (23/12/2018)

- Split everything into folders
- Added __init__.py files to create packages
- Created data folder
    - Added curr_screen_resolution.txt file to keep track of resolution
    - Added stocks.txt file to keep track of stocks
        - Stock file consists of Name, Amount, Price
        - Stocks have to be added manually
    - Moved user_data.txt into data folder
- Create src folder which contains all code
    - Added tkinter_load_pages which contains Main class
    - Added tkinter_page_definitions which contains all page definitions
    and is imported to tkinter_load_pages
    - Added tkinter_product_page_definitions which will hold the definitions
    for product pages (To be implemented)
- Created test_scripts folder which holds all dump scripts
- Created main.py which imports src.tkinter_load_pages and contains mainloop
(did this so I can work more with tkinter_load_pages without initializing mainloop)
-
Update 1.2 (23/12/2018)

- Added Products Page
    - Implemented next gen concept of displaying items from stocks.txt file
        - Displays Name, In Stock and Price each systematically displayed using
        next gen code
    - Added buttons to click and buy products (To be implemented)
- Added Menu Page which the user goes to after logging in
    - Can go to add items to sale or go to buy items
- Added Supply Page where the user can fill out form to supply product
    - Includes name, amount, price and description (for later)
    - Next gen code writes this all to file
        - Changed utils.write_file for it to write newline first as it caused
        formatting problems
    - Implemented Text Widget to get long input for description
    - Added input parameters
- Added next gen concept of refreshing pages after leaving them
    - Very complex :)

Update 1.3 (23/12/2018)

- Added a lot of stuff but can't be bothered to document; tl;dr:
- Added Products page where you can buy items
    - In products page you can also delete items and resupply existing items
    - Items added to the stocks.txt through suppply page will also be displayed here
- Added Model Page class to systematically generate pages for individual items (very advanced)
    - This is done in products page while generating it to maximize efficiency
    - Added delete button to delete existing stocks (using my very sophisticated algorithm) :)
    - Added Buy button to buy items 
    - Added button to update existing stock
- Added cart page where all your orders are placed
    - This includes the checkout function which finalizes all orders and updates stocks
        - This means that it decreases the amount of stocks depending on
        how much you buy (very advanced)





