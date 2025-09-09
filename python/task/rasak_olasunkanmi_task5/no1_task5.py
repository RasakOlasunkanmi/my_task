# Task1:  Create and Display

# Step 1 - Ask the user to enter three favorite Nigerian dishes (one at a time).
# Step 2 - Store them in a tuple called dishes.
# Step 3 - Print the tuple in a single line, separating items with commas.
# Step 4 - Use the \n escape sequence to print each dish on a new line.

dish1 = input("Enter your favorite dish: ")
dish2 = input("Enter your favorite dish: ")
dish3 = input("Enter your favorite dish: ")
dishes = (dish1, dish2, dish3)
print(dishes)
print(",".join(dishes))
print("\n".join(dishes))