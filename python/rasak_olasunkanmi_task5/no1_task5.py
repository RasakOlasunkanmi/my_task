# Task1:  Create and Display

# Step 1 - Ask the user to enter three favorite Nigerian dishes (one at a time).
# Step 2 - Store them in a tuple called dishes.
# Step 3 - Print the tuple in a single line, separating items with commas.
# Step 4 - Use the \n escape sequence to print each dish on a new line.

# Method 1
dish1 = input("Enter your favorite dish: ")
dish2 = input("Enter your favorite dish: ")
dish3 = input("Enter your favorite dish: ")
dishes = (dish1, dish2, dish3)
print(dishes)
print(",".join(dishes))
print("\n".join(dishes))

# Method 2
dishes = ()
for i in range(3):
    dish = input(f"Enter your favorite Nigerian dish {i + 1}: ")
    dishes += (dish,)
print("Your favorite Nigerian dishes are:")
print(", ".join(dishes))
print("\n".join(dishes))