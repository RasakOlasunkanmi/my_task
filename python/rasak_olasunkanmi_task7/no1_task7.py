# Task1: Student Bio Data Storage
# Create a program that collects student bio-data from user input (name, age, gender, courses) and stores it in a dictionary.
#   - Courses should be stored as a list.
#   - Display the bio-data neatly using escape sequences.
# - Requirements:
#   - Use `input()` to collect details.
#   - Use dictionary operations `(dict[key] = value)` to store data.
#   - Use `print()` formatting with `\n` and `\t` for better output.

# Method 1
student_bio_data = {}
# Collecting student bio-data from user input
student_bio_data["name"] = input("Enter your name: ")
student_bio_data["age"] = input("Enter your age: ")
student_bio_data["gender"] = input("Enter your gender: ")
student_bio_data["courses"] = input("Enter your courses (comma-separated): ")
# Splitting the courses input into a list
student_bio_data["courses"] = student_bio_data["courses"].split(',')
# Displaying the bio-data neatly
print("\nStudent Bio Data:")
print(f"Name: \t\t{student_bio_data['name']}")
print(f"Age: \t\t{student_bio_data['age']}")
print(f"Gender: \t{student_bio_data['gender']}")
print(f"Courses: \t{(student_bio_data['courses'])}")