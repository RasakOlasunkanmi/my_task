# Task 5: Student Score Tracker

# Step 1 - Ask the user for 3 student names.
# Step 2 - For each student, ask for their score.
# Step 3 - Store the results in two lists (one for names, one for scores).
# Step 4 - Print a formatted output showing Name — Score, aligned neatly.
# - Tips: You are to start by creating two empty lists.

# Method 1
names = [
    input("Enter name of student 1: "),
    input("Enter name of student 2: "),
    input("Enter name of student 3: ")
]

scores = [
    input(f"Enter score for {names[0]}: "),
    input(f"Enter score for {names[1]}: "),
    input(f"Enter score for {names[2]}: ")
]

print("\nStudent Scores:")
print("\n".join(f"{n:<20} — {s}" for n, s in zip(names, scores)))