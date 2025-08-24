# Task4: Create a Unique Voters Registration System
# Step 1 - Ask for voter names and store in a set.
# Step 2 - If a voter tries to register twice, display a warning.
# Step 3 - After registration, display the total number of unique voters.

voter1 = input("Enter your name to register as a voter: ")
voter2 = input("Enter your name to register as a voter: ")
voter3 = input("Enter your name to register as a voter: ")
voter4 = input("Enter your name to register as a voter: ")
voter5 = input("Enter your name to register as a voter: ")
voters = {voter1, voter2, voter3, voter4, voter5}
if len(voters) < 5:
    print("Warning: Some names were duplicates and not added.")
print("Total unique voters registered:", len(voters))
print("Unique voters:", sorted(voters))