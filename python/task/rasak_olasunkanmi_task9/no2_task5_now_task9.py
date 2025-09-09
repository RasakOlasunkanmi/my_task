# Task2: Tuple and Input

# Step 1 - Ask the user for 5 best friends’ names.
# Step 2 - Store them in a tuple friends.
# Step 3 - Print the tuple in reverse order.

friends = ()
for i in range(5):
    friend = input(f"Enter the name of your best friend {i + 1}: ")
    friends += (friend,)
print("Your best friends in reverse order are: ")
print(friends[::-1])