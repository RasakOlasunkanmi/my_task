# Task1: Student Bio Data Storage
# Create a program that collects student bio-data from user input (name, age, gender, courses) and stores it in a dictionary.
#   - Courses should be stored as a list.
#   - Display the bio-data neatly using escape sequences.
# - Requirements:
#   - Use `input()` to collect details.
#   - Use dictionary operations `(dict[key] = value)` to store data.
#   - Use `print()` formatting with `\n` and `\t` for better output.

student_bio_data = {}
fields = ["name", "age", "gender", "courses"]

try:
    for field in fields:
        value = input(f"Enter your {field}: ")

        # Special check for age
        if field == "age":
            if not value.isdigit():
                raise ValueError("Age must be a number.")
            value = int(value)  # convert to integer

        student_bio_data[field] = value

    # Convert courses into a list (comma-separated input)
    student_bio_data["courses"] = student_bio_data["courses"].split(',')

except ValueError as e:
    print(f"Input Error: {e}")

finally:
    if student_bio_data:
        print("\nStudent Bio Data:")
        print(f"Name: \t\t{student_bio_data.get('name', 'N/A')}")
        print(f"Age: \t\t{student_bio_data.get('age', 'N/A')}")
        print(f"Gender: \t{student_bio_data.get('gender', 'N/A')}")
        print(f"Courses: \t{student_bio_data.get('courses', 'N/A')}")
    else:
        print("\nNo valid data collected.")