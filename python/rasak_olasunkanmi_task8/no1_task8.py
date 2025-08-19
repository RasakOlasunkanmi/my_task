# Task1
# - Explain each output of the program below.
# - Give 3 usecases or cenarios where you can apply the program below.
# - Write the code for 1 of the 3 use cases.

num1 = int(input("Enter first number: "))   # Ask the user to enter a number as integer
num2 = int(input("Enter second number: "))  # Ask the user to enter a number as integer
print(f"{num1} == {num2}: {num1 == num2}")  # Display the compared result of checking the equality of num1 and num2
# Output 4 == 5 : False which means num1 and num2 are not equal, hence the result False

print(f"{num1} != {num2} : {num1 != num2}")  # Output: True; which means num1 and num2 are not equal, hence the result True

print(f"{num1} > {num2} : {num1 > num2}")    # Output: False; which means num1 < num2 hence the result

print(f"{num1} < {num2} : {num1 < num2}")    # Output: True; which means num2 > num1 hence the result True

#  Give 3 usecases or cenarios where you can apply the program below.
# Use Case 1: Grading System - Compare two students' scores to determine who performed better.
# Use Case 2: Access Control - Check if a user's age meets the minimum requirement for registration.
# Use Case 3: Inventory Management - Compare quantities of two products to decide which needs restocking.
# Use Case 2: Access Control - Check if a user's age meets the minimum requirement for registration.

min_age = 18     # min age declaration
user_age = int(input("Enter your age: "))    # Ask the user to enter age
print(f"Access granted: {user_age >= min_age}")   # Display the 
