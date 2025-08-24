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

# Prompt user for citizenship
citizenship = input("Are you a citizen of Nigeria? (yes/no): ").strip().lower()

# Prompt user for enrollment status
enrollment = input("Are you a registered, full-time undergraduate student in a recognized Nigerian university? (yes/no): ").strip().lower()

# Prompt user for other scholarships
other_scholarship = input("Are you currently receiving any other scholarship from an entity in the Oil and Gas industry? (yes/no): ").strip().lower()

# Prompt user for academic qualifications
waec_distinctions = int(input("How many distinctions (A or B) did you get in relevant WAEC/WASSCE subjects (including English and Mathematics)? "))

# Use a loop to collect subjects
subjects = []
for i in range(5):  # allow up to 5 subjects
    subj = input(f"Enter distinction subject {i+1}: ").strip().title()
    if subj:  # allow blank to stop early
        subjects.append(subj)

print("\nSubjects with distinctions:")
print("\n".join(f"{i+1}. {subj}" for i, subj in enumerate(subjects)))

# Ensure 'English' and 'Mathematics' are included
has_required_subjects = "English" in subjects and "Mathematics" in subjects

# Update eligibility
is_eligible = (
    citizenship == "yes"
    and enrollment == "yes"
    and other_scholarship == "no"
    and waec_distinctions >= 5
    and has_required_subjects
)

# Display candidate information and eligibility status
print("\nFederal Government Scholarship Eligibility Check")
print(f"Candidate: {name}")
print(f"Citizenship: {citizenship.title()}")
print(f"Enrollment: {enrollment.title()}")
print(f"Other Oil & Gas Scholarship: {other_scholarship.title()}")
print(f"WAEC/WASSCE Distinctions: {waec_distinctions}")
print(f"Eligible: {is_eligible}")

print(f"\nFinal Eligibility (including subject check): {is_eligible}")