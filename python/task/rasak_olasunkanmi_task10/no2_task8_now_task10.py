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

# Function to safely get yes/no responses
def get_yes_no(prompt):
    while True:
        response = input(prompt).strip().lower()
        if response in ["yes", "no"]:
            return response
        print("Invalid input. Please enter 'yes' or 'no'.")

# Function to safely get an integer input
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

# Prompt user for their name
name = input("Enter your name: ").strip().title()

# Citizenship
citizenship = get_yes_no("Are you a citizen of Nigeria? (yes/no): ")

# Enrollment
enrollment = get_yes_no("Are you a registered, full-time undergraduate student in a recognized Nigerian university? (yes/no): ")

# Other scholarship
other_scholarship = get_yes_no("Are you currently receiving any other scholarship from an entity in the Oil and Gas industry? (yes/no): ")

# WAEC distinctions
waec_distinctions = get_int("How many distinctions (A or B) did you get in relevant WAEC/WASSCE subjects (including English and Mathematics)? ")

# Subjects with distinctions (up to 5, stop early if blank)
subjects = []
for i in range(5):
    subj = input(f"Enter distinction subject {i+1} (press Enter to stop): ").strip().title()
    if subj:
        subjects.append(subj)
    else:
        break

if not subjects:
    print("\nNo subjects entered! Candidate is not eligible.")
    subjects = []

print("\nSubjects with distinctions:")
for i, subj in enumerate(subjects, start=1):
    print(f"{i}. {subj}")

# Ensure English and Mathematics are included
has_required_subjects = "English" in subjects and "Mathematics" in subjects

# Eligibility check
is_eligible = (
    citizenship == "yes"
    and enrollment == "yes"
    and other_scholarship == "no"
    and waec_distinctions >= 5
    and has_required_subjects
)

# Display results
print("\nFederal Government Scholarship Eligibility Check")
print(f"Candidate: {name}")
print(f"Citizenship: {citizenship.title()}")
print(f"Enrollment: {enrollment.title()}")
print(f"Other Oil & Gas Scholarship: {other_scholarship.title()}")
print(f"WAEC/WASSCE Distinctions: {waec_distinctions}")
print(f"Eligible: {is_eligible}")

print(f"\nFinal Eligibility (including subject check): {is_eligible}")
