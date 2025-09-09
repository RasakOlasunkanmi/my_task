# Task6: Attendance Tracker
# - Write a Python program that;
# Step 1 - Stores the days of the week in a tuple.
# Step 2 - Stores the months of the year in another tuple.
# Step 3 - Asks the user to enter:
# Step 4 - Student’s name
# Step 5 - Gender
# Step 6 - Course Track
# Step 7 - Current month number (1-12)
# Step 8 - Current day number (1-7)

days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
student_name = input("Enter student's name: ")
gender = input("Enter student's gender: ")
course_track = input("Enter student's course track: ")
current_month = int(input("Enter current month number (1-12): "))
current_day = int(input("Enter current day number (1-7): "))
print(f"Student Name: {student_name}")
print(f"Gender: {gender}")
print(f"Course Track: {course_track}")
print(f"Current month number: {months[current_month - 1]}")
print(f"Current day: {days[current_day - 1]}")