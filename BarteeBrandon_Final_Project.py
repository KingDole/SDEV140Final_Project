# This is a pizza ordering app for Tony's Pizzeria. The customer will be able
# to create and place orders for pizzas with the available toppings. There is
# a second window that details the order and gives a total price.

# Import tkinter
import tkinter as tk

# Define a function that creates a new window for pizza creation
def createNewPizza():

    # Disable the Create New Pizza button
    bt_new_pizza["state"] = "disabled"

    # Create a new window
    create_pizza_window = tk.Tk()
    create_pizza_window.resizable(False, False)
    create_pizza_window.geometry("500x500")
    create_pizza_window.title("Create a new pizza")

    # Add Labels for Page Title, Crust, Sauce, Cheese, Toppings, Meat and Non-Meat
    pizza_creation_title = tk.Label(create_pizza_window, text = "New Pizza")
    crust_options = tk.Label(create_pizza_window, text = "Crust")
    sauce_options = tk.Label(create_pizza_window, text = "Sauce")
    cheese_options = tk.Label(create_pizza_window, text = "Cheese")
    topping_options = tk.Label(create_pizza_window, text = "Toppings")
    meat_options = tk.Label(create_pizza_window, text = "Meat")
    not_meat_options = tk.Label(create_pizza_window, text = "Non-Meat")

    # Organize the Labels to a grid
    pizza_creation_title.grid(row = 0, column = 0)
    crust_options.grid(row = 1, column = 0)
    sauce_options.grid(row = 3, column = 0)
    cheese_options.grid(row = 5, column = 0)
    topping_options.grid(row = 7, column = 0)
    meat_options.grid(row = 8, column = 0)
    not_meat_options.grid(row = 8, column = 1)

    # Add radio buttons for crusts
    crusts = ""
    regular_crust = tk.Radiobutton(create_pizza_window, text = "Regular", variable = crusts)
    pretzal_crust = tk.Radiobutton(create_pizza_window, text = "Pretzal", variable = crusts)
    stuffed_crust = tk.Radiobutton(create_pizza_window, text = "Stuffed(+$1.00)", variable = crusts)
    regular_crust.grid(row = 2, column = 0)
    pretzal_crust.grid(row = 2, column = 1)
    stuffed_crust.grid(row = 2, column = 2)

    # Add radio buttons for sauce
    sauces = ""
    no_sauce = tk.Radiobutton(create_pizza_window, text = "None", variable = sauces)
    regular_sauce = tk.Radiobutton(create_pizza_window, text = "Regular", variable = sauces)
    extra_sauce = tk.Radiobutton(create_pizza_window, text = "Extra", variable = sauces)
    no_sauce.grid(row = 4, column = 0)
    regular_sauce.grid(row = 4, column = 1)
    extra_sauce.grid(row = 4, column = 2)

    # Add radio butons for cheese
    cheese = ""
    no_cheese = tk.Radiobutton(create_pizza_window, text = "None", variable = cheese)
    regular_cheese = tk.Radiobutton(create_pizza_window, text = "Regular", variable = cheese)
    extra_cheese = tk.Radiobutton(create_pizza_window, text = "Extra(+$1.00)", variable = cheese)
    no_cheese.grid(row = 6, column = 0)
    regular_cheese.grid(row = 6, column = 1)
    extra_cheese.grid(row = 6, column = 2)

    # Create a button to enable the Create New Pizza button, close the window and add the pizza to window 1
    bt_add_pizza = tk.Button(text = "Add Pizza")
    
    
# Create first window
home_window = tk.Tk()
home_window.resizable(False, True)
home_window.geometry("500x500")
home_window.title("Tony's Pizzeria")

# Add title banner and pricing information
home_page_name_banner = tk.Label(home_window, text = "Welcome to Tony's Pizzeria!")
home_page_name_banner.place(relx = 0.5, rely = 0.03, anchor = "center")
home_page_pricing1 = tk.Label(home_window, text = "Pizzas are $10 plus $0.50 per topping.")
home_page_pricing1.place(relx = 0.5, rely = 0.07, anchor = "center")
home_page_pricing2 = tk.Label(home_window, text = "Get stuffed crust or extra cheese for another $1!")
home_page_pricing2.place(relx = 0.5, rely = 0.11, anchor = "center")

# Add a button that starts the pizza creation process
bt_new_pizza = tk.Button(text = "Create New Pizza", command = createNewPizza)
bt_new_pizza.place(relx = 0.5, rely = 0.17, anchor = "center")

# Create column labels for pizza description, quantity and price
pizza_description = tk.Label(home_window, text = "Pizza Description", font = "Arial 12 underline")
pizza_description.place(relx = 0.15, rely = 0.24, anchor = "center")
pizza_quantity = tk.Label(home_window, text = "Qty", font = "Arial 12 underline")
pizza_quantity.place(relx = 0.65, rely = 0.24, anchor = "center")
pizza_price = tk.Label(home_window, text = "Price", font = "Arial 12 underline")
pizza_price.place(relx = 0.85, rely = 0.24, anchor = "center")

# Start the window
home_window.mainloop()


