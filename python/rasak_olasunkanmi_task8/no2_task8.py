# Task2
# - Comment the code below appropriately, and using doctring, explain what the code is doing.
# -  Adapt the code to the case below.

# - Federal Government Scholarship Key Eligibility Requirements:
#   - Citizenship:
#     - Applicant must be a citizen of Nigeria. 
#   - Enrollment:
#     - Must be a registered, full-time undergraduate student in a recognized Nigerian university. 
#   - Other Scholarships:
#     - Applicants cannot be currently receiving any other scholarship from an entity in the Oil and Gas industry, whether national or international. 
#   - Academic Qualification:
#     - For undergraduate courses, applicants usually need five distinctions (As and Bs) in relevant subjects in their WAEC/WASSCE (May/June) exams, including English and Mathematics.

# name = input("Enter your name: ")   # Ask the user to enter name
# age = int(input("Enter your age: "))  # Ask the user to enter age as integer
# score = int(input("Enter your test score: "))  # Ask the user to enter test score as integer
# eligibility = (age < 18) and (score > 70)    # Checking if the student qualify or not
# print(f"Candidate: {name}\nAge: {age}\nScore: {score}\nEligible: {eligibility}")   #Display the user details above and eligibility status each on a new line

# subjects = 
name = input("Enter your name: ")
age = int(input("Enter your age: "))
nationality = input("Enter your nationality: ").title()
enrollment = input("Are you a full-time undergraduate student in a recognized Nigerian university?\nEnter (yes/no): ").lower()
other_scholarships = input("Are you currently receiving any other scholarship from an entity in the Oil and Gas industry, whether national or international?\nEnter (yes/no): ").lower()
academic_qualification = input("Do you have 'A's' or 'B's' in relevant subjects in your WAEC/WASSCE (May/June) exams, including English and Mathematics?\nEnter (yes/no): ").lower()
eligibility = (nationality == "Nigeria") and (enrollment == "yes") and (other_scholarships == "no") and (academic_qualification == "yes")
print(f"Candidate: {name}\nAge: {age}\nNationality: {nationality}\nFull-time in Nigeria recognized school: {enrollment}\nOn other scholarship (oil & gas): {other_scholarships}\nAcademic Qualification: {academic_qualification}\nEligibility: {eligibility}")


"""
The code above collects user input for a scholarship eligibility check.

Steps:
1. Prompts the user to enter their name, age, and test score.
2. Converts age and score inputs to integers.
3. Checks eligibility based on two criteria:
   - Age must be less than 18.
   - Test score must be greater than 70.
4. Displays the candidate's details and eligibility status, each on a new line.
"""