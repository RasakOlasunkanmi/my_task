# Task3: Days and Activities Pairing
# - Store days of the week in a tuple and ask the user to input an activity for three specific days.
#   - Use dictionary comprehension to pair days and activities.
#   - Print the dictionary.
# - Requirements:
#   - Use a tuple for days.
#   - Use {day: activity for day, activity in `zip(..., ...)`}.
#   Tip: Research on how to use `zip()`

days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")

# Collect 3 activities using a loop
activities = []
for i in range(3):
    activity = input(f"Enter activity {i+1}: ")
    activities.append(activity)

# Select first 3 days
selected_days = days[:3]

# Create dictionary mapping days to activities
day_activity = {day: activity for day, activity in zip(selected_days, activities)}

print("\nDay-Activity Dictionary:")
print(day_activity)

# Print each activity for the selected days
for day, activity in day_activity.items():
    print(f"On {day}, your activity is: {activity}")

# Print again using join
print("\n".join([f"On {day}, your activity is: {activity}" for day, activity in day_activity.items()]))