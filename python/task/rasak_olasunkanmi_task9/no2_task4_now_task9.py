# Task 2: Shopping List Manager
# Step 1- Create an empty list.
# Step 2 - Ask the user to enter 3 shopping items (one by one).
# Step 3 - Add them to the list.
# Step 4 - Display the list as a single string, separated by commas.

shopping_list = []
for i in range(3):
    item = input(f"Enter shopping item {i + 1}: ")
    shopping_list.append(item)
print("Shopping List: " + ", ".join(shopping_list))