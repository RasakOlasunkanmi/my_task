# Compulsory Task(but not graded): Student Profile Builder
# - This program collects student details, academic scores, hobbies, and guardian info, stores them in a nested dictionary, and performs automatic calculations and transformations using dictionary comprehension, tuple unpacking, and set operations.
# Collect student details.

def create_student_profile():
    try:
        # Collect student details
        student_name = input("Enter student name: ").strip()
        student_age = int(input("Enter student age: "))   # may raise ValueError
        student_class = input("Enter student class: ").strip()

        # Collect academic scores
        subjects = ["Math", "English", "Science"]
        scores = {}
        for subject in subjects:
            while True:  # keep asking until valid input
                try:
                    score = float(input(f"Enter score for {subject}: "))
                    if 0 <= score <= 100:
                        scores[subject] = score
                        break
                    else:
                        print("Score must be between 0 and 100.")
                except ValueError:
                    print("Invalid input. Please enter a numeric score.")

        # Calculate average score and pass/fail status
        average_score = sum(scores.values()) / len(scores)
        score_status = {subject: ("Pass" if score >= 50 else "Fail")
                        for subject, score in scores.items()}

        # Collect hobbies
        hobbies_input = input("Enter hobbies separated by commas: ").strip()
        hobbies = set(h.strip().title() for h in hobbies_input.split(",") if h.strip())
        school_hobbies = {"Football", "Music", "Art", "Science Club"}
        common_hobbies = hobbies & school_hobbies

        # Collect guardian info
        while True:
            guardian_info = input("Enter guardian name and phone separated by a comma: ").strip()
            try:
                guardian_name, guardian_phone = (item.strip() for item in guardian_info.split(","))
                break
            except ValueError:
                print("Invalid format. Please enter as: Name, Phone")

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

    except ValueError:
        print("Invalid input detected. Please restart and enter the correct details.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Run program
if __name__ == "__main__":
    create_student_profile()