# Compulsory Task(but not graded): Student Profile Builder
# - This program collects student details, academic scores, hobbies, and guardian info, stores them in a nested dictionary, and performs automatic calculations and transformations using dictionary comprehension, tuple unpacking, and set operations.
# Collect student details

student_name = input("Enter student name: ")
student_age = int(input("Enter student age: "))
student_class = input("Enter student class: ")

# Collect academic scores
subjects = ["Math", "English", "Science"]
scores = {}
for subject in subjects:
    score = float(input(f"Enter score for {subject}: "))
    scores[subject] = score

# Calculate average score using dictionary comprehension
average_score = sum(scores.values()) / len(scores)
score_status = {subject: ("Pass" if score >= 50 else "Fail") for subject, score in scores.items()}

# Collect hobbies and perform set operations
hobbies = set(input("Enter hobbies separated by commas: ").split(","))
school_hobbies = {"Football", "Music", "Art", "Science Club"}
common_hobbies = hobbies & school_hobbies

# Collect guardian info using tuple unpacking
guardian_info = input("Enter guardian name and phone separated by a comma: ")
guardian_name, guardian_phone = (item.strip() for item in guardian_info.split(","))

# Build nested dictionary profile
student_profile = {
    "details": {
        "name": student_name,
        "age": student_age,
        "class": student_class
    },
    "scores": scores,
    "average_score": average_score,
    "score_status": score_status,
    "hobbies": list(hobbies),
    "common_hobbies": list(common_hobbies),
    "guardian": {
        "name": guardian_name,
        "phone": guardian_phone
    }
}

# Display student profile
print("\nStudent Profile:")
for key, value in student_profile.items():
    print(f"{key}: {value}")