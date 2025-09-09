# Task4: Tuple Unpacking
# - Ask a user for their;
# Step 1 - First name
# Step 2 - Age
# Step 3 - Favorite color
# Step 4 - Home town
# Step 5 - Store them in a tuple profile and unpack into variables.
# Step 6 - Print and use  escape sequence to align each piece of information nicely.

user_first_name = input("Enter your first name: ")
user_age = input("Enter your age: ")
user_favorite_color = input("Enter your favorite color: ")
user_home_town = input("Enter your home town: ")

identity = (user_first_name, user_age, user_favorite_color, user_home_town)

print("Your identity details are:")
for item in identity:
    print(item)