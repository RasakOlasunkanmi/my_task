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
months = ("January", "February", "March", "April", "May", "June", 
          "July", "August", "September", "October", "November", "December")

# Fields we want from the user
fields = ["student's name", "student's gender", "student's course track", 
          "current month number (1-12)", "current day number (1-7)"]

responses = []

try:
    # Collect inputs with loop
    for field in fields:
        responses.append(input(f"Enter {field}: "))

    # Unpack responses
    student_name, gender, course_track, current_month, current_day = responses
    current_month = int(current_month)
    current_day = int(current_day)

    # Validate month and day
    if not (1 <= current_month <= 12):
        raise ValueError("Month number must be between 1 and 12.")
    if not (1 <= current_day <= 7):
        raise ValueError("Day number must be between 1 and 7.")

    # Display results
    print(f"\nStudent Name: {student_name}")
    print(f"Gender: {gender}")
    print(f"Course Track: {course_track}")
    print(f"Current month: {months[current_month - 1]}")
    print(f"Current day: {days[current_day - 1]}")

except ValueError as ve:
    print(f"Input Error: {ve}")
except Exception as e:
    print(f"Unexpected Error: {e}")
finally:
    print("\tProgram Finished")