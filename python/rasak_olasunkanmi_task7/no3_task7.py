# Task3: Days and Activities Pairing
# - Store days of the week in a tuple and ask the user to input an activity for three specific days.
#   - Use dictionary comprehension to pair days and activities.
#   - Print the dictionary.
# - Requirements:
#   - Use a tuple for days.
#   - Use {day: activity for day, activity in `zip(..., ...)`}.
#   Tip: Research on how to use `zip()`

days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
activity1 = input("Enter activity: ")
activity2 = input("Enter activity: ")
activity3 = input("Enter activity: ")
selected_days = days[:3]
activities = [activity1, activity2, activity3]
day_activity = {day: activity for day, activity in zip(selected_days, activities)}
print(day_activity)

for day, activity in day_activity.items():
    print(f"On {day}, your activity is: {activity}")