# Task5: Modify Tuple Indirectly
# Ask a user to enter three items for their shopping list.
# Step 1 - Store in a tuple shopping_list.
# Step 2 - Convert it to a list, then ask for two more items to add.
# Step 3 - Convert back to a tuple and print the updated list using join() to display items separated by " | ".

shopping_list = ()

for i in range(5):
    item = input(f"Enter shopping item {i + 1}: ")
    shopping_list += (item,)

print("\nYour complete shopping list:")
print("\n".join(shopping_list))