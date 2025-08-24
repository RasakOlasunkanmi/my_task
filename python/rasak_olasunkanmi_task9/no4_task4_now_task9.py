# Task 4: Name Organizer
# Step 1 - Ask the user to enter 5 names (separated by spaces).
# Step 2 - Convert all names to lowercase
# Step 3 - Sort the list alphabetically.
# Step 4 - Display them one name per line.
# -Tips: use `range()`,`sort()`, `for`, `in`, `split()`, `len()`,`lower()` 

names_input = input("Enter 5 names separated by spaces: ")
names_list = names_input.split(",")
names_list = [name.lower() for name in names_list]
names_list.sort()
for i in range(len(names_list)):
    print(names_list[i])