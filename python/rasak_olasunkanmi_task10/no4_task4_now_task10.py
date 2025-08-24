# Task 4: Name Organizer
# Step 1 - Ask the user to enter 5 names (separated by spaces).
# Step 2 - Convert all names to lowercase
# Step 3 - Sort the list alphabetically.
# Step 4 - Display them one name per line.
# -Tips: use `range()`,`sort()`, `for`, `in`, `split()`, `len()`,`lower()` 

#  Method 3- using try-except-finally

try:
    names_input = input("Enter 5 names separated by commas: ")

    if not names_input.strip():
        raise ValueError("You must enter at least one name.")

    names_list = names_input.split(",")                 # split into list
    names_list = [name.lower() for name in names_list]  # convert to lowercase
    names_list.sort()                                   # sort alphabetically

    print("\n".join(names_list))

except ValueError as ve:
    print(f"Input Error: {ve}")
except Exception as e:
    print(f"Unexpected Error: {e}")
finally:
    print("\tProgram finished")