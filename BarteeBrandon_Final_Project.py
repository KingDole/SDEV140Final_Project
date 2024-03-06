# This is a pizza ordering app for Tony's Pizzeria. The customer will be able
# to create and place orders for pizzas with the available toppings. There is
# a second window that details the order and gives a total price.

# Import tkinter
import tkinter as tk

# Instantiate variables
pizza_num = 4
cost_list = []

# Create a new window and hide it
create_pizza_window = tk.Tk()
create_pizza_window.resizable(False, False)
create_pizza_window.geometry("500x500")
create_pizza_window.title("Create a new pizza")

bg2 = tk.PhotoImage(file = r"D:\SDEV 140\Final Project\Pizza.png")
bg_label2 = tk.Label(create_pizza_window, image = bg2)
bg_label2.place(x = 0, y = 0)

crusts = tk.StringVar(create_pizza_window, "Regular")
sauces = tk.StringVar(create_pizza_window, "No")
cheeses = tk.StringVar(create_pizza_window, "No")
create_pizza_window.withdraw()

# Define a function that creates a new window for pizza creation
def createNewPizza():

    # Bring the second window back
    create_pizza_window.deiconify()
    
    # Disable the Create New Pizza button
    bt_new_pizza["state"] = "disabled"

    # Add Labels for Page Title, Crust, Sauce, Cheese, Toppings, Meat and Non-Meat
    pizza_creation_title = tk.Label(create_pizza_window, text = "New Pizza").grid(sticky = "W", row = 0, column = 0)
    crust_options = tk.Label(create_pizza_window, text = "Crust").grid(sticky = "W", row = 2, column = 0)
    sauce_options = tk.Label(create_pizza_window, text = "Sauce").grid(sticky = "W", row = 5, column = 0)
    cheese_options = tk.Label(create_pizza_window, text = "Cheese").grid(sticky = "W", row = 8, column = 0)
    topping_options = tk.Label(create_pizza_window, text = "Toppings").grid(sticky = "W", row = 11, column = 0)
    meat_options = tk.Label(create_pizza_window, text = "Meat").grid(sticky = "W", row = 12, column = 0)
    not_meat_options = tk.Label(create_pizza_window, text = "Non-Meat").grid(sticky = "W", row = 12, column = 1)

    # Add radio buttons for crusts
    global crusts
    regular_crust = tk.Radiobutton(create_pizza_window, text = "Regular", variable = crusts, value = "Regular").grid(sticky = "W", row = 3, column = 0)
    pretzal_crust = tk.Radiobutton(create_pizza_window, text = "Pretzal", variable = crusts, value = "Pretzal").grid(sticky = "W", row = 3, column = 1)
    stuffed_crust = tk.Radiobutton(create_pizza_window, text = "Stuffed(+$1.00)", variable = crusts, value = "Stuffed").grid(sticky = "W", row = 3, column = 2)

    # Add radio buttons for sauce
    global sauces
    no_sauce = tk.Radiobutton(create_pizza_window, text = "No", variable = sauces, value = "No").grid(sticky = "W", row = 6, column = 0)
    regular_sauce = tk.Radiobutton(create_pizza_window, text = "Regular", variable = sauces, value = "Regular").grid(sticky = "W", row = 6, column = 1)
    extra_sauce = tk.Radiobutton(create_pizza_window, text = "Extra", variable = sauces, value = "Extra").grid(sticky = "W", row = 6, column = 2)

    # Add radio buttons for cheese
    global cheeses
    no_cheese = tk.Radiobutton(create_pizza_window, text = "No", variable = cheeses, value = "No").grid(sticky = "W", row = 9, column = 0)
    regular_cheese = tk.Radiobutton(create_pizza_window, text = "Regular", variable = cheeses, value = "Regular").grid(sticky = "W", row = 9, column = 1)
    extra_cheese = tk.Radiobutton(create_pizza_window, text = "Extra(+$1.00)", variable = cheeses, value = "Extra").grid(sticky = "W", row = 9, column = 2)

    # Add radio buttons for meats
    pepp_var = tk.IntVar()
    saus_var = tk.IntVar()
    ham_var = tk.IntVar()
    baco_var = tk.IntVar()
    chick_var = tk.IntVar()
    top_pepp = tk.Checkbutton(create_pizza_window, text = "Pepperoni", variable = pepp_var).grid(sticky = "W", row = 13, column = 0)
    top_saus = tk.Checkbutton(create_pizza_window, text = "Sausage", variable = saus_var).grid(sticky = "W", row = 14, column = 0)
    top_ham = tk.Checkbutton(create_pizza_window, text = "Ham", variable = ham_var).grid(sticky = "W", row = 15, column = 0)
    top_baco = tk.Checkbutton(create_pizza_window, text = "Bacon", variable = baco_var).grid(sticky = "W", row = 16, column = 0)
    top_chick = tk.Checkbutton(create_pizza_window, text = "Chicken", variable = chick_var).grid(sticky = "W", row = 17, column = 0)
    
    # Add radio buttons for non-meats
    mush_var = tk.IntVar()
    oliv_var = tk.IntVar()
    pine_var = tk.IntVar()
    onio_var = tk.IntVar()
    anch_var = tk.IntVar()
    top_mush = tk.Checkbutton(create_pizza_window, text = "Mushrooms", variable = mush_var).grid(sticky = "W", row = 13, column = 1)
    top_oliv = tk.Checkbutton(create_pizza_window, text = "Olives", variable = oliv_var).grid(sticky = "W", row = 14, column = 1)
    top_pine = tk.Checkbutton(create_pizza_window, text = "Pineapples", variable = pine_var).grid(sticky = "W", row = 15, column = 1)
    top_onio = tk.Checkbutton(create_pizza_window, text = "Onions", variable = onio_var).grid(sticky = "W", row = 16, column = 1)
    top_anch = tk.Checkbutton(create_pizza_window, text = "Anchovies", variable = anch_var).grid(sticky = "W", row = 17, column = 1)

    # List of toppings
    
        
    # Create a function to add the pizza to window 1 and close the window
    def closeWin2():

        global pizza_num
        toppings_cost = 0
        pizza_num = pizza_num + 1
        
        #toppings_list = [pepp_var.get(), saus_var.get(), ham_var.get(), baco_var.get(), chick_var.get(), mush_var.get(), oliv_var.get(), pine_var.get(), onio_var.get(), anch_var.get()]
        #toppings_text = ["Pepperoni, ", "Sausage, ", "Ham, ", "Bacon, ", "Chicken ", "Mushrooms, ", "Olives, ", "Pineapple, ", "Onion, ", "Anchovie, "]
        toppings_dict = {"Pepperoni, ":pepp_var.get(), "Sausage, ":saus_var.get(), "Ham, ":ham_var.get(), "Bacon, ":baco_var.get(), "Chicken, ":chick_var.get(),
                         "Mushroom, ":mush_var.get(), "Olives, ":oliv_var.get(), "Pineapple, ":pine_var.get(), "Onion, ":onio_var.get(), "Anchovies, ":anch_var.get()}
                         
        selected_toppings = []       
        
        #for i in toppings_list:
            #if i == 1:
                #selected_toppings.append(toppings_text[i])
                #toppings_cost += 0.50
        for topping in toppings_dict:
            if toppings_dict[topping] == 1:
                selected_toppings.append(topping)
                toppings_cost += 0.50
                
        if crusts.get() == "Stuffed":
            toppings_cost += 1
            
        if cheeses.get() == "Extra":
            toppings_cost += 1
            
        pizza_cost = 10 + toppings_cost
        pizza_price = ('%.2f' % (10 + toppings_cost))
        cost_list.append(pizza_cost)

        selected_toppings_string = ''.join(map(str, selected_toppings))
        description_string = crusts.get() + " Crust, " + sauces.get() + " Sauce, " + cheeses.get() + " Cheese, " + selected_toppings_string        
           
        new_pizza_description = tk.Label(home_window, text = description_string).grid(sticky = "W", row = pizza_num, column = 0, columnspan = 2)
        new_pizza_quantity = tk.Label(home_window, text = "1").grid(row = pizza_num, column = 2)
        new_pizza_cost = tk.Label(home_window, text = "$" + pizza_price).grid(row = pizza_num, column = 3)
        bt_new_pizza["state"] = "normal"
        create_pizza_window.withdraw()
        
    # Create a button to enable the Create New Pizza button, close the window and add the pizza to window 1
    bt_add_pizza = tk.Button(create_pizza_window, text = "Add Pizza", command = closeWin2)
    bt_add_pizza.place(relx = 0.5, rely = 0.8, anchor = "center")
    
    
# Create first window
home_window = tk.Toplevel()
home_window.resizable(True, True)
home_window.geometry("1200x675")
home_window.title("Tony's Pizzeria")

home_window.columnconfigure(0, minsize = 300, weight = 0)
home_window.columnconfigure(1, minsize = 300, weight = 0)
home_window.columnconfigure(2, minsize = 300, weight = 0)
home_window.columnconfigure(3, minsize = 300, weight = 0)

bg = tk.PhotoImage(file = r"D:\SDEV 140\Final Project\heavy_face.png")
bg_label = tk.Label(home_window, image = bg)
bg_label.place(x = 0, y = 0)

# Add title banner and pricing information
home_page_name_banner = tk.Label(home_window, text = "Welcome to Tony's Pizzeria!")
home_page_name_banner.grid(row = 0, column = 0, columnspan = 2)
home_page_pricing1 = tk.Label(home_window, text = "Pizzas are $10 plus $0.50 per topping.")
home_page_pricing1.grid(row = 1, column = 0, columnspan = 2)
home_page_pricing2 = tk.Label(home_window, text = "Get stuffed crust or extra cheese for another $1!")
home_page_pricing2.grid(row = 2, column = 0, columnspan = 2)

# Add a button that starts the pizza creation process
bt_new_pizza = tk.Button(home_window, text = "Create New Pizza", command = createNewPizza)
bt_new_pizza.grid(row = 3, column = 1, columnspan = 2)

# Create column labels for pizza description, quantity and price
pizza_description = tk.Label(home_window, text = "Pizza Description", font = "Arial 12 underline")
pizza_description.grid(sticky = "W", row = 4, column = 0, columnspan = 2)
pizza_quantity = tk.Label(home_window, text = "Qty", font = "Arial 12 underline")
pizza_quantity.grid(row = 4, column = 2)
pizza_price = tk.Label(home_window, text = "Price", font = "Arial 12 underline")
pizza_price.grid(row = 4, column = 3)

# Create function to calculate total quantity and order cost
def getTotals():
    global pizza_num
    new_pizzas = pizza_num - 4
    total_pizzas = tk.Label(home_window, text =  "Total Pizzas: " + str(new_pizzas), font = "Arial 12").grid(row = 0, column = 2, columnspan = 2)
    final_cost = ('%.2f' % sum(cost_list))
    total_cost = tk.Label(home_window, text = "Total Cost: $" + str(final_cost), font = "Arial 12").grid(row = 1, column = 2, columnspan = 2)
    
# Create a button to generate the total quantity and cost of the order
bt_total = tk.Button(home_window, text = "Total", command = getTotals)
bt_total.place(relx = .9, rely = .9, anchor = "center")

# Start the window
home_window.mainloop()


