
# Task 5: Student Score Tracker

# Step 1 - Ask the user for 3 student names.
# Step 2 - For each student, ask for their score.
# Step 3 - Store the results in two lists (one for names, one for scores).
# Step 4 - Print a formatted output showing Name — Score, aligned neatly.
# - Tips: You are to start by creating two empty lists.

names = []
scores = []
print("Enter the names and scores of 3 students:")
for i in range(3):
    name = input(f"Enter name of student {i + 1}: ")
    score = input(f"Enter score for {name}: ")
    names.append(name)
    scores.append(score)
print("\nStudent Scores:")
for i in range(len(names)):
    print(f"{names[i]:<20} — {scores[i]}")