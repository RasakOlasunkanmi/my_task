# Task5: Store Inventory Update
# - Create a dictionary called store with items and their available quantities. Example:
# store = {"Book": 10, "Pen": 20, "Bag": 5}
# - Ask the user to input the item they want to buy (e.g., "Pen").
# - Ask the user to input the quantity they want to purchase.
# - Use the assignment operator -= to update (reduce) the item quantity in the dictionary.
# - Print the updated dictionary in this format:
# Before purchase: {'Book': 10, 'Pen': 20, 'Bag': 5}
# After purchase: {'Book': 10, 'Pen': 18, 'Bag': 5}


# Initialize store inventory with items and quantities
store = {"Book": 10, "Pen": 20, "Bag": 5}
print("Before purchase:", store)   # Display inventory before purchase
item = input("Enter the item you want to buy: ")   # Get item name from user
quantity = int(input("Enter the quantity you want to purchase: "))  # Get quantity from user
store[item] -= quantity  # Reduce the quantity of the selected item
print("After purchase:", store)  # Display inventory after purchase


"""
This prompt is a simple store inventory system.
- Initializes a dictionary `store` with items and their available quantities.
- Displays the inventory before purchase.
- Prompts the user to input the item they wish to buy and the quantity.
- Updates the inventory by reducing the quantity of the selected item using the -= operator.
- Prints the updated inventory after the purchase.
"""