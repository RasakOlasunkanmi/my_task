# Task4: Student Record
# - Ask the user to input their name and age, then store them in the dictionary.
# - Add a list of scores (e.g., [70, 85, 90]) to the dictionary.
# - Use a comparison operator to check if the student has passed (average score >= 50). Save the result (True/False) in the dictionary under the key "passed".
# - Use a logical operator to check if the student is a teenager (age between 13 and 19). Save the result as "teenager".
# - Print out the complete record in this format:
# Student Record:
# Name: John
# Age: 16
# Scores: [70, 85, 90]
# Passed: True
# Teenager: True

# Create an empty list to store multiple student records
students = []

# Ask how many students to enter (with error handling)
while True:
    try:
        num_students = int(input("How many students do you want to enter? "))
        if num_students <= 0:
            print("Please enter a positive number of students.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

for _ in range(num_students):
    # Create an empty dictionary for each student
    student = {}

    # Get name
    student['name'] = input("Enter your name: ")

    # Get age with error handling
    while True:
        try:
            age = int(input("Enter your age: "))
            if age <= 0:
                print("Age must be positive. Try again.")
                continue
            student['age'] = age
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for age.")

    # Add a predefined list of scores to the dictionary
    student['scores'] = [70, 85, 90]

    # Calculate the average score
    average_score = sum(student['scores']) / len(student['scores'])

    # Check if the student has passed (average score >= 50) and store the result
    student['passed'] = average_score >= 50

    # Check if the student is a teenager (age between 13 and 19 inclusive) and store the result
    student['teenager'] = 13 <= student['age'] <= 19

    # Append the student record to the list
    students.append(student)

# Print all student records
print("\nAll Student Records:")
for student in students:
    print("\n")
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"Scores: {student['scores']}")
    print(f"Passed: {student['passed']}")
    print(f"Teenager: {student['teenager']}")