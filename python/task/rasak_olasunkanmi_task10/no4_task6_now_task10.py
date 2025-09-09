# Task4: Create a Unique Voters Registration System
# Step 1 - Ask for voter names and store in a set.
# Step 2 - If a voter tries to register twice, display a warning.
# Step 3 - After registration, display the total number of unique voters.

try:
    names = set()
    for i in range(5):
        voter = input(f"Enter name of voter {i + 1}: ").strip()
        if not voter:  # check if input is empty
            print("You must enter a valid name!")
        elif voter in names:
            print(f"Warning: {voter} is already registered.")
        else:
            names.add(voter)

except Exception as e:
    print("An unexpected error occurred:", e)

finally:
    print("\nTotal number of unique voters registered:", len(names))
    print("Registered voters:", ", ".join(sorted(names)))