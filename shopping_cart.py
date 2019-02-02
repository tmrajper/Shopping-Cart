# Author: Tarik Rajper

#Used to exit program
import sys

class ItemToPurchase:

    # Constructor with parameters: name, price, quantity, and description
    def __init__(self, item_name = "none", item_price = 0, item_quantity = 0, item_description = "none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    # Sets name
    def set_name(self, new_name):
        self.item_name = new_name

    # Sets Price
    def set_price(self, new_price):
        self.item_price = new_price
    
    # Sets quantity
    def set_quantity(self, new_quant):
        self.item_quantity = new_quant

    # Sets description
    def set_desc(self, new_desc):
        self.item_description = new_desc

    # Returns name
    def get_name(self):
        return self.item_name

    # Returns price
    def get_price(self):
        return self.item_price
    
    # Returns quantity
    def get_quantity(self):
        return self.item_quantity

    # Returns description
    def get_desc(self):
        return self.item_description

    # Returns name, quantity, price, and total price as a string
    def print_item_cost(self):
        return self.item_name + " " + str(self.item_quantity) +  " @ $" + str(self.item_price) + " = $" + str(self.item_quantity * self.item_price)

    # Returns Item name and description as one string
    def print_item_description(self):
        return self.item_name + ": " + self.item_description

class ShoppingCart(ItemToPurchase):
    
    # Constructor for Shopping Cart class with parameters: Customer name, date, and cart
    def __init__(self, customer_name = "none", current_date = "January 1, 2016", cart_items = []):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    # Adds item to cart
    def add_item(self, ItemToPurchase):
        self.cart_items.append(ItemToPurchase)

    # Removes item from cart
    def remove_item(self, item_name):
        not_found = False

        if len(self.cart_items) != 0:
            for i in range(0, len(self.cart_items)):
                if self.cart_items[i].get_name().lower() == item_name.lower():
                    del self.cart_items[i]
                    not_found = False
                    break
                else:
                    not_found = True

            if not_found == True:
                print("Item Not Found!")

        else:
            print("Cart is Empty!")

    # Modifies quantity of item in cart
    def modify_item(self, ItemToPurchase):
        not_found = False

        if len(self.cart_items) != 0:
            for i in range(0, len(self.cart_items)):
                if ItemToPurchase.get_name().lower() == self.cart_items[i].get_name().lower():
                    ItemToPurchase = self.cart_items[i]
                    new_quant = int(input("Enter new quantity: "))
                    del self.cart_items[i]
                    ItemToPurchase.set_quantity(new_quant)
                    self.add_item(ItemToPurchase)
                    not_found = False
                    break
                else:
                    not_found = True

            if not_found == True:
                print("Item Not Found!")

        else:
            print("Cart is empty!")

    # Returns total items in cart
    def get_items_in_cart(self):
        total_quant = 0
        for i in range(0, len(self.cart_items)):
            total_quant += self.cart_items[i].get_quantity()
        return total_quant

    # Returns total cost of cart
    def get_cost_of_cart(self):
        total_cost = 0
        for i in range(0, len(self.cart_items)):
            total_cost += self.cart_items[i].get_price() * self.cart_items[i].get_quantity()
        return total_cost

    # Prints total length of cart
    def print_total(self):
        return len(self.cart_items)

    # Prints desscriptions of each item
    def print_descriptions(self):
        if len(self.cart_items) != 0:
            for i in range(0, len(self.cart_items)):
                print(self.cart_items[i].print_item_description())
        else:
            print("Cart is empty")

    # Prints information of each item
    def print_names(self):
        if len(self.cart_items) != 0:
            for i in range(0, len(self.cart_items)):
                print(self.cart_items[i].print_item_cost())
        else:
            print("Cart is empty")

    # Checks if cart is empty
    def is_empty(self):
        if len(self.cart_items) == 0:
            return True
        return False

    # Returns customer name and date
    def get_username(self):
        return self.customer_name + "'s Shopping Cart - " + self.current_date

# Main method, runs program
def main():
    name = input("Enter your name: ")
    date = input("Enter current Date: ")
    global cart
    cart = []
    Cart = ShoppingCart(name.title(), date, cart)
    print_menu(Cart)


# Prints user menu
def menu():
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change Item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - quit")

# UI for menu, uses shopping cart class as a parameter
def print_menu(shopping_cart):

    while True:
        menu()
        choice = input("Choose an option: ")

        if choice == 'a':
            print("ADD ITEM TO CART")
            item_name = input("Enter item name: ")
            price = float(input("Enter item price: "))
            quant = int(input("Enter item quantity: "))
            desc = input("Enter item description: ")
            new_item = ItemToPurchase(item_name.title(), price, quant, desc)
            shopping_cart.add_item(new_item)
        elif choice == 'r':
            if shopping_cart.is_empty() == True:
                print("Cart is Empty!")
            else:
                print("REMOVE ITEM FROM CART")
                remove = input("Enter item to remove: ")
                shopping_cart.remove_item(remove)
        elif choice == 'c':
            if shopping_cart.is_empty() == True:
                print("Cart is Empty!")
            else:
                print("CHANGE ITEM QUANTITY")
                new_name = input("Enter item name: ")
                new_item = ItemToPurchase()
                new_item.set_name(new_name)
                shopping_cart.modify_item(new_item)
        elif choice == 'i':
            if shopping_cart.is_empty() == True:
                print("Cart is Empty!")
            else:
                print("OUTPUT ITEMS' DESCRIPTION")
                print(shopping_cart.get_username())
                print("Item Descriptions")
                shopping_cart.print_descriptions()
        elif choice == 'o':
            if shopping_cart.is_empty() == True:
                print("Cart is Empty!")
            else:
                print("OUTPUT SHOPPING CART")
                print(shopping_cart.get_username())
                print("Number of Items: " + str(shopping_cart.get_items_in_cart()))
                shopping_cart.print_names()
                print("Total: $" + str(shopping_cart.get_cost_of_cart()))
        elif choice == 'q':
            break
        else:
            print("Enter a valid option!")

    sys.exit()

# Runs main
if __name__ == '__main__':
    main()

"""
Output

Enter your name: John Doe
Enter current Date: February 1, 2016
a - Add item to cart
r - Remove item from cart
c - Change Item quantity
i - Output items' descriptions
o - Output shopping cart
q - quit
Choose an option: a
ADD ITEM TO CART
Enter item name: Nike Romaleos
Enter item price: 189
Enter item quantity: 2
Enter item description: Volt color, Weightlifting shoes
a - Add item to cart
r - Remove item from cart
c - Change Item quantity
i - Output items' descriptions
o - Output shopping cart
q - quit
Choose an option: a
ADD ITEM TO CART
Enter item name: Chocolate Chips
Enter item price: 3
Enter item quantity: 5
Enter item description: Semi-sweet
a - Add item to cart
r - Remove item from cart
c - Change Item quantity
i - Output items' descriptions
o - Output shopping cart
q - quit
Choose an option: a
ADD ITEM TO CART
Enter item name: Powerbeats 2 Headphones
Enter item price: 128
Enter item quantity: 1
Enter item description: Bluetooth headphones
a - Add item to cart
r - Remove item from cart
c - Change Item quantity
i - Output items' descriptions
o - Output shopping cart
q - quit
Choose an option: o
OUTPUT SHOPPING CART
John Doe's Shopping Cart - February 1, 2016
Number of Items: 8
Nike Romaleos 2 @ $189.0 = $378.0
Chocolate Chips 5 @ $3.0 = $15.0
Powerbeats 2 Headphones 1 @ $128.0 = $128.0
Total: $521.0
a - Add item to cart
r - Remove item from cart
c - Change Item quantity
i - Output items' descriptions
o - Output shopping cart
q - quit
Choose an option: i
OUTPUT ITEMS' DESCRIPTION
John Doe's Shopping Cart - February 1, 2016
Item Descriptions
Nike Romaleos: Volt color, Weightlifting shoes
Chocolate Chips: Semi-sweet
Powerbeats 2 Headphones: Bluetooth headphones
a - Add item to cart
r - Remove item from cart
c - Change Item quantity
i - Output items' descriptions
o - Output shopping cart
q - quit
Choose an option: r
REMOVE ITEM FROM CART
Enter item to remove: Chocolate Chips
a - Add item to cart
r - Remove item from cart
c - Change Item quantity
i - Output items' descriptions
o - Output shopping cart
q - quit
Choose an option: o
OUTPUT SHOPPING CART
John Doe's Shopping Cart - February 1, 2016
Number of Items: 3
Nike Romaleos 2 @ $189.0 = $378.0
Powerbeats 2 Headphones 1 @ $128.0 = $128.0
Total: $506.0
a - Add item to cart
r - Remove item from cart
c - Change Item quantity
i - Output items' descriptions
o - Output shopping cart
q - quit
Choose an option: c
CHANGE ITEM QUANTITY
Enter item name: Nike Romaleos
Enter new quantity: 3
a - Add item to cart
r - Remove item from cart
c - Change Item quantity
i - Output items' descriptions
o - Output shopping cart
q - quit
Choose an option: o
OUTPUT SHOPPING CART
John Doe's Shopping Cart - February 1, 2016
Number of Items: 4
Powerbeats 2 Headphones 1 @ $128.0 = $128.0
Nike Romaleos 3 @ $189.0 = $567.0
Total: $695.0
a - Add item to cart
r - Remove item from cart
c - Change Item quantity
i - Output items' descriptions
o - Output shopping cart
q - quit
Choose an option: q

-----------------------------------------------------

Enter your name: Tarik Rajper
Enter current Date: November 11, 2018
a - Add item to cart
r - Remove item from cart
c - Change Item quantity
i - Output items' descriptions
o - Output shopping cart
q - quit
Choose an option: a
ADD ITEM TO CART
Enter item name: Wrist Wraps
Enter item price: 15
Enter item quantity: 1
Enter item description: Weightlifting wraps, Black and red
a - Add item to cart
r - Remove item from cart
c - Change Item quantity
i - Output items' descriptions
o - Output shopping cart
q - quit
Choose an option: a
ADD ITEM TO CART
Enter item name: Layrite Pomade
Enter item price: 18
Enter item quantity: 2
Enter item description: Superhold pomade
a - Add item to cart
r - Remove item from cart
c - Change Item quantity
i - Output items' descriptions
o - Output shopping cart
q - quit
Choose an option: 
Enter a valid option!
a - Add item to cart
r - Remove item from cart
c - Change Item quantity
i - Output items' descriptions
o - Output shopping cart
q - quit
Choose an option: a
ADD ITEM TO CART
Enter item name: Ultraboosts 
Enter item price: 180
Enter item quantity: 1
Enter item description: Version: 3.0, Triple White
a - Add item to cart
r - Remove item from cart
c - Change Item quantity
i - Output items' descriptions
o - Output shopping cart
q - quit
Choose an option: o
OUTPUT SHOPPING CART
Tarik Rajper's Shopping Cart - November 11, 2018
Number of Items: 4
Wrist Wraps 1 @ $15.0 = $15.0
Layrite Pomade 2 @ $18.0 = $36.0
Ultraboosts 1 @ $180.0 = $180.0
Total: $231.0
a - Add item to cart
r - Remove item from cart
c - Change Item quantity
i - Output items' descriptions
o - Output shopping cart
q - quit
Choose an option: i
OUTPUT ITEMS' DESCRIPTION
Tarik Rajper's Shopping Cart - November 11, 2018
Item Descriptions
Wrist Wraps: Weightlifting wraps, Black and red
Layrite Pomade: Superhold pomade
Ultraboosts: Version: 3.0, Triple White
a - Add item to cart
r - Remove item from cart
c - Change Item quantity
i - Output items' descriptions
o - Output shopping cart
q - quit
Choose an option: r
REMOVE ITEM FROM CART
Enter item to remove: Layrite pomade
a - Add item to cart
r - Remove item from cart
c - Change Item quantity
i - Output items' descriptions
o - Output shopping cart
q - quit
Choose an option: o
OUTPUT SHOPPING CART
Tarik Rajper's Shopping Cart - November 11, 2018
Number of Items: 2
Wrist Wraps 1 @ $15.0 = $15.0
Ultraboosts 1 @ $180.0 = $180.0
Total: $195.0
a - Add item to cart
r - Remove item from cart
c - Change Item quantity
i - Output items' descriptions
o - Output shopping cart
q - quit
Choose an option: i
OUTPUT ITEMS' DESCRIPTION
Tarik Rajper's Shopping Cart - November 11, 2018
Item Descriptions
Wrist Wraps: Weightlifting wraps, Black and red
Ultraboosts: Version: 3.0, Triple White
a - Add item to cart
r - Remove item from cart
c - Change Item quantity
i - Output items' descriptions
o - Output shopping cart
q - quit
Choose an option: c
CHANGE ITEM QUANTITY
Enter item name: Ultraboosts
Enter new quantity: 2
a - Add item to cart
r - Remove item from cart
c - Change Item quantity
i - Output items' descriptions
o - Output shopping cart
q - quit
Choose an option: o
OUTPUT SHOPPING CART
Tarik Rajper's Shopping Cart - November 11, 2018
Number of Items: 3
Wrist Wraps 1 @ $15.0 = $15.0
Ultraboosts 2 @ $180.0 = $360.0
Total: $375.0
a - Add item to cart
r - Remove item from cart
c - Change Item quantity
i - Output items' descriptions
o - Output shopping cart
q - quit
Choose an option: i
OUTPUT ITEMS' DESCRIPTION
Tarik Rajper's Shopping Cart - November 11, 2018
Item Descriptions
Wrist Wraps: Weightlifting wraps, Black and red
Ultraboosts: Version: 3.0, Triple White
a - Add item to cart
r - Remove item from cart
c - Change Item quantity
i - Output items' descriptions
o - Output shopping cart
q - quit
Choose an option: q

"""
