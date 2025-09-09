# Task4: Create a Unique Voters Registration System
# Step 1 - Ask for voter names and store in a set.
# Step 2 - If a voter tries to register twice, display a warning.
# Step 3 - After registration, display the total number of unique voters.

name1 = input("Enter your name to register as a voter: ")
name2 = input("Enter your name to register as a voter: ")
name3 = input("Enter your name to register as a voter: ")
name4 = input("Enter your name to register as a voter: ")
name5 = input("Enter your name to register as a voter: ")
names = {name1, name2, name3, name4, name5}
names = set(names)  # Ensure names are unique
for name in [name1, name2, name3, name4, name5]:
    if name not in names:
        print(f"Warning: {name} is already registered.")
    else:
        names.add(name)
print("\nTotal number of unique voters registered:", len(names))