# Task5: Modify Tuple Indirectly
# Ask a user to enter three items for their shopping list.
# Step 1 - Store in a tuple shopping_list.
# Step 2 - Convert it to a list, then ask for two more items to add.
# Step 3 - Convert back to a tuple and print the updated list using join() to display items separated by " | ".

shopping_list1 = input("Enter your first list: ")
shopping_list2 = input("Enter your second list: ")
shopping_list3 = input("Enter your third list: ")
shopping_list = (shopping_list1, shopping_list2, shopping_list3)
new_shopping_list = list(shopping_list)
new_shopping_list.append(input("Enter your fourth list: "))
new_shopping_list.append(input("Enter your fifth list: "))
new_shopping_list = tuple(new_shopping_list)
print("\n".join(new_shopping_list))