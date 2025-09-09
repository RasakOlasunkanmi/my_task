# Task1:  Create and Display

# Step 1 - Ask the user to enter three favorite Nigerian dishes (one at a time).
# Step 2 - Store them in a tuple called dishes.
# Step 3 - Print the tuple in a single line, separating items with commas.
# Step 4 - Use the \n escape sequence to print each dish on a new line.

dishes = ()
for i in range(3):
    dish = input(f"Enter your favorite Nigerian dish {i + 1}: ")
    dishes += (dish,)
print("Your favorite Nigerian dishes are:")
print(", ".join(dishes))
print("\n".join(dishes))