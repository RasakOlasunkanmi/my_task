# Task4: Tuple Unpacking
# - Ask a user for their;
# Step 1 - First name
# Step 2 - Age
# Step 3 - Favorite color
# Step 4 - Home town
# Step 5 - Store them in a tuple profile and unpack into variables.
# Step 6 - Print and use  escape sequence to align each piece of information nicely.

try:
    identity = ()
    fields = ["first name", "age", "favorite color", "home town"]

    for field in fields:
        value = input(f"Enter your {field}: ")
        if not value.strip():   # check for empty input
            raise ValueError(f"{field.capitalize()} cannot be empty.")
        identity += (value,)

    print("\nYour identity details are:")
    for item in identity:
        print(item)

except ValueError as ve:
    print(f"Input Error: {ve}")
except Exception as e:
    print(f"Unexpected Error: {e}")
finally:
    print("\tProgram finished")