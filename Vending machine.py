# -*- coding: utf-8 -*-
"""
Vending machine assignment
"""

# Class definition for the VendingMachine
class VendingMachine:
    def __init__(self):  # Constructor method to set up the initial state of an object
        # Dictionary of products with product number as the key, and name and price as values
        self.products = {
            1: {"name": "Cola", "price": 1.50},
            2: {"name": "Chips", "price": 1.00},
            3: {"name": "Chocolate", "price": 0.75},
            4: {"name": "Bread", "price": 1.50},
            5: {"name": "Tea", "price": 1.00},
        }
        # Attribute to keep track of the current balance in the vending machine
        self.balance = 0.0

    def display_products(self):  # Method to display available products in the vending machine
        print("Welcome to the Vending Machine!")
        print("Available Products:")
        for key, product in self.products.items():
            print(f"{key}. {product['name']} - ${product['price']:.2f}")

    def insert_coins(self):  # Method to handle the process of inserting coins into the vending machine
        while True:
            try:
                coins = float(input("Insert coins (enter 0 to finish): $"))
                if coins == 0:
                    break
                elif coins < 0:
                    print("Please enter a positive amount.")
                else:
                    # Update the balance with the inserted coins
                    self.balance += coins
                    print(f"Current Balance: ${self.balance:.2f}")
            except ValueError:
                print("Invalid input. Please enter a valid amount.")

    def select_product(self):  # Method to handle the process of selecting and purchasing a product
        while True:
            try:
                choice = int(input("Enter the number of the product you want to purchase: "))
                if choice not in self.products:
                    print("Invalid selection. Please choose a valid product.")
                else:
                    selected_product = self.products[choice]
                    if self.balance >= selected_product["price"]:
                        # Deduct the price of the selected product from the balance
                        self.balance -= selected_product["price"]
                        print(f"Enjoy your {selected_product['name']}! Remaining Balance: ${self.balance:.2f}")
                    else:
                        print("Insufficient funds. Please insert more coins.")
                    break
            except ValueError:
                print("Invalid input. Please enter a valid product number.")

    def run(self):  # Method to initiate and run the vending machine process
        self.display_products()
        self.insert_coins()
        self.select_product()

# Check if the script is being run directly (not imported as a module)
if __name__ == "__main__":
    # Create an instance of the VendingMachine class
    vending_machine = VendingMachine()
    # Run the vending machine process
    vending_machine.run()
