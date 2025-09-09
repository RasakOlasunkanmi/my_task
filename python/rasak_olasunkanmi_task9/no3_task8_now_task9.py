# Task3: Online Store Cart Calculation
# - Create a list of items (e.g., "Book", "Pen", "Bag") and another list of prices (e.g., 500, 100, 2000).
# - Start with an empty cart total (cart_total = 0).
# - Use assignment operators (+=) to add the price of some items into cart_total.
# - Print the list of items and the total price using an f-string like this:
# ```
# Items: ['Book', 'Pen', 'Bag']
# Total Price: ₦600
# ```

# items and prices lists represent available products and their costs
items = ["Book", "Pen", "Bag"]
prices = [500, 100, 2000]

# cart_total is initialized to zero to store the total cost of selected items
cart_total = 0

# Select first two items (Book and Pen) using a loop
selected_indices = [0, 1]  # choosing Book and Pen

for i in selected_indices:
    cart_total += prices[i]

# Printing the selected items ("Book" and "Pen")
print(f"Items: {[items[i] for i in selected_indices]}")

# Printing the total price of selected items using an f-string
print(f"Total Price: ₦{cart_total}")