# Task 2: Shopping List Manager
# Step 1- Create an empty list.
# Step 2 - Ask the user to enter 3 shopping items (one by one).
# Step 3 - Add them to the list.
# Step 4 - Display the list as a single string, separated by commas.

# Method 1
shopping_list = []
Item_1 = input("Enter your shopping item 1: ")
Item_2 = input("Enter your shopping item 2: ")
Item_3 = input("Enter your shopping item 3: ")
shopping_list = [Item_1, Item_2, Item_3]
print(f"Item 1: {Item_1}, Item 2: {Item_2}, Item 3: {Item_3}")

# Method 2
shopping_list = []
for i in range(3):
    item = input(f"Enter shopping item {i + 1}: ")
    shopping_list.append(item)
print("Shopping List: " + ", ".join(shopping_list))

