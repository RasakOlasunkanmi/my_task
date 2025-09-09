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

while True:
    print("\nBefore purchase:", store)   # Display inventory before purchase
    
    # Get item name and quantity from user
    item = input("Enter the item you want to buy (or 'exit' to quit): ")
    if item.lower() == "exit":
        break
    quantity = int(input("Enter the quantity you want to purchase: "))
    
    # Reduce the quantity of the selected item
    store[item] -= quantity  
    
    # Display inventory after purchase
    print("After purchase:", store)