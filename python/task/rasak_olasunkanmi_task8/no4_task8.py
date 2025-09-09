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

# Create an empty dictionary to store student information
student = {}

# Ask the user to input their name and store it in the dictionary
student['name'] = input("Enter your name: ")

# Ask the user to input their age and store it in the dictionary (convert input to integer)
student['age'] = int(input("Enter your age: "))

# Add a predefined list of scores to the dictionary
student['scores'] = [70, 85, 90]

# Calculate the average score
average_score = sum(student['scores']) / len(student['scores'])

# Check if the student has passed (average score >= 50) and store the result
student['passed'] = average_score >= 50

# Check if the student is a teenager (age between 13 and 19 inclusive) and store the result
student['teenager'] = 13 <= student['age'] <= 19

# Print out the complete student record in the specified format
print("Student Record:")
print(f"Name: {student['name']}")
print(f"Age: {student['age']}")
print(f"Scores: {student['scores']}")
print(f"Passed: {student['passed']}")
print(f"Teenager: {student['teenager']}")