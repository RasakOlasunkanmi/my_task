# Task2: Tuple and Input

# Step 1 - Ask the user for 5 best friends’ names.
# Step 2 - Store them in a tuple friends.
# Step 3 - Print the tuple in reverse order.

friend_1 = input("Enter your best friend's name: ")
friend_2 = input("Enter your best friend's name: ")
friend_3 = input("Enter your best friend's name: ")
friend_4 = input("Enter your best friend's name: ")
friend_5 = input("Enter your best friend's name: ")
friends = (friend_1, friend_2, friend_3, friend_4, friend_5)
reversed_tuple = friends[::-1]
print(reversed_tuple)