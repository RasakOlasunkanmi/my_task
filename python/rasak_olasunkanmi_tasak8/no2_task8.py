#  Task2
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


# Prompt user for their name
name = input("Enter your name: ")

# Prompt user for their age and convert input to integer
age = int(input("Enter your age: "))

# Prompt user for their test score and convert input to integer
score = int(input("Enter your test score: "))

# Check eligibility: candidate must be under 18 and have a score above 70
eligibility = (age < 18) and (score > 70)

# Display candidate information and eligibility status
print(f"Candidate: {name}\nAge: {age}\nScore: {score}\nEligible: {eligibility}")


"""
This script collects candidate information and checks eligibility for a scholarship
based on age and test score. It prompts the user for their name, age, and test score,
then determines eligibility if the candidate is under 18 years old and has a score above 70.
Finally, it prints the candidate's details and eligibility status.
"""

# Prompt user for citizenship
citizenship = input("Are you a citizen of Nigeria? (yes/no): ").strip().lower()

# Prompt user for enrollment status
enrollment = input("Are you a registered, full-time undergraduate student in a recognized Nigerian university? (yes/no): ").strip().lower()

# Prompt user for other scholarships
other_scholarship = input("Are you currently receiving any other scholarship from an entity in the Oil and Gas industry? (yes/no): ").strip().lower()

# Prompt user for academic qualifications
waec_distinctions = int(input("How many distinctions (A or B) did you get in relevant WAEC/WASSCE subjects (including English and Mathematics)? "))

# Check eligibility based on all requirements
is_eligible = (
    citizenship == "yes" and
    enrollment == "yes" and
    other_scholarship == "no" and
    waec_distinctions >= 5
)

# Display candidate information and eligibility status
print("\nFederal Government Scholarship Eligibility Check")
print(f"Candidate: {name}")
print(f"Citizenship: {citizenship.title()}")
print(f"Enrollment: {enrollment.title()}")
print(f"Other Oil & Gas Scholarship: {other_scholarship.title()}")
print(f"WAEC/WASSCE Distinctions: {waec_distinctions}")
print(f"Eligible: {is_eligible}")

# Prompt user to enter up to nine WAEC/WASSCE subjects with distinctions (including English and Mathematics), without using a loop or conditionals
print("\nEnter the names of up to nine WAEC/WASSCE subjects in which you received a distinction (A or B), separated by commas.")
print("You must include 'English' and 'Mathematics'.")

subjects_input = input("Subjects (comma-separated): ")
subjects = [s.strip().title() for s in subjects_input.split(",")][:9]

print("\nSubjects with distinctions:")
print("\n".join(f"{i+1}. {subj}" for i, subj in enumerate(subjects)))
# Ensure 'English' and 'Mathematics' are included in the list of subjects with distinctions
has_required_subjects = "English" in subjects and "Mathematics" in subjects

# Update eligibility to include subject check
is_eligible = (
    citizenship == "yes" and
    enrollment == "yes" and
    other_scholarship == "no" and
    waec_distinctions >= 5 and
    has_required_subjects
)

print(f"\nFinal Eligibility (including subject check): {is_eligible}")



"""
This section adapts the eligibility check to Federal Government Scholarship requirements.
It verifies citizenship, enrollment status, absence of other Oil & Gas scholarships, and
academic qualifications (minimum five distinctions in WAEC/WASSCE including English and Mathematics).
"""