# Task1
# - Explain each output of the program below.
# - Give 3 usecases or cenarios where you can apply the program below.
# - Write the code for 1 of the 3 use cases.


num1 = int(input("Enter first number: "))  # Prompt user for first number, convert input to integer, and assign to num1

num2 = int(input("Enter second number: "))  # Prompt user for second number, convert input to integer, and assign to num2

print(f"{num1} == {num2} : {num1 == num2}")  # Display whether num1 is equal to num2 (True/False)

print(f"{num1} != {num2} : {num1 != num2}")  # Display whether num1 is not equal to num2 (True/False)

print(f"{num1} > {num2} : {num1 > num2}")   # Display whether num1 is greater than num2 (True/False)

print(f"{num1} < {num2} : {num1 < num2}")   # Display whether num1 is less than num2 (True/False)


# - Give 3 usecases or cenarios where you can apply the program below.
# Usecase 1: Grading System - Compare two students' scores to determine the higher grade.
# Usecase 2: Access Control - Check if a user's age meets the minimum registration.
# Usecase 3: Inventory Management - Compare quantities of two products restocking.

# Usecase 2: Access Control - Check if a user's age meets the minimum registration.

min_age = 20  # Set the minimum age required for access
user_age = int(input("Enter your age: "))   # Prompt the user to input their age and convert it to an integer
print(f"Access granted: {user_age >= min_age}")  # Print whether access is granted based on age comparison