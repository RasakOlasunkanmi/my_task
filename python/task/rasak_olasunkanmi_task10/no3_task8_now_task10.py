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

# Show items with indices
print("Available items:")
for i, item in enumerate(items):
    print(f"{i}: {item} - ₦{prices[i]}")

try:
    # User chooses items by entering indices (comma-separated)
    selected_input = input("\nEnter the indices of items you want to buy (comma-separated): ")
    selected_indices = [int(x.strip()) for x in selected_input.split(",")]

    # Check for invalid indices
    for i in selected_indices:
        if i < 0 or i >= len(items):
            raise IndexError(f"Invalid index {i}. Please choose between 0 and {len(items)-1}.")
    
    # Calculate total
    for i in selected_indices:
        cart_total += prices[i]

    # Print results
    print(f"\nItems: {[items[i] for i in selected_indices]}")
    print(f"Total Price: ₦{cart_total}")

except ValueError:
    print("Error: Please enter numbers only, separated by commas.")
except IndexError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")