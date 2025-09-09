# Task6
# - The Federal Government of Nigeria has set the minimum age for admission into federal tertiary institutions at 16 years old for the 2025/2026 academic session, according to the Minister of Education, Dr. Tunji Alausa. This policy, announced at the 2025 JAMB policy meeting, replaces the previous 18-year minimum age requirement. 

# - For the 2025/2026 academic session, the University of Lagos (UNILAG) requires candidates to have a minimum UTME score of 200 to be eligible for the Post-UTME screening. The Post-UTME itself is an online screening exercise. UNILAG does not release specific departmental cut-off marks before the screening. The departmental cut-off marks are determined after the Post-UTME, based on merit and the performance of candidates in both UTME and the Post-UTME. 

# Breakdown of the Admission Process:
# 1. UTME:
# Candidates must score 200 or above in the UTME and choose UNILAG as their first choice. 
# 2. O'Level Requirements:
# Candidates must also have five (5) credit passes at one sitting in relevant O'Level subjects, including English Language and Mathematics. 
# 3. Post-UTME:
# Eligible candidates participate in the university's online Post-UTME screening. 
# 4. Departmental Cut-off Marks:
# After the Post-UTME, the university determines departmental cut-off marks based on merit and overall performance
# (This can range from 200 to 320). 
# 5. Final Admission:
# Candidates who meet the departmental cut-off marks are offered admission. 

# - Write a program to account for all of the conditions above, Such that when a user imputes all their required details, they are told if they will be legible for admission or not.

    # Define the function to check admission eligibility
def check_admission_eligibility():
        # Print the program header
        print("UNILAG Admission Eligibility Checker (2025/2026 Session)")

        # Prompt user to enter their age and convert input to integer
        age = int(input("Enter your age: "))
        # Prompt user to enter their UTME score and convert input to integer
        utme_score = int(input("Enter your UTME score: "))
        # Ask if UNILAG is their first choice and normalize input to lowercase
        first_choice = input("Is UNILAG your first choice institution? (yes/no): ").strip().lower()
        # Ask for number of O'Level credit passes at one sitting and convert to integer
        num_credits = int(input("How many O'Level credit passes do you have at one sitting?: "))
        # Ask if user has credit in English Language and normalize input
        english = input("Do you have credit in English Language? (yes/no): ").strip().lower()
        # Ask if user has credit in Mathematics and normalize input
        maths = input("Do you have credit in Mathematics? (yes/no): ").strip().lower()
        # Prompt user to enter their Post-UTME score and convert input to integer
        post_utme_score = int(input("Enter your Post-UTME score (after online screening): "))
        # Prompt user to enter their departmental cut-off mark and convert input to integer
        dept_cutoff = int(input("Enter your departmental cut-off mark (between 200 and 320): "))

        # List of boolean checks for each eligibility criterion
        checks = [
            age >= 16,  # Check if age is at least 16
            utme_score >= 200,  # Check if UTME score is at least 200
            first_choice == "yes",  # Check if UNILAG is first choice
            num_credits >= 5,  # Check if at least 5 credit passes
            english == "yes",  # Check for credit in English Language
            maths == "yes",  # Check for credit in Mathematics
            200 <= dept_cutoff <= 320,  # Check if departmental cut-off is valid
            ((utme_score + post_utme_score) // 2) >= dept_cutoff  # Check if aggregate meets cut-off
        ]

        # Corresponding messages for failed checks
        messages = [
            "You are NOT eligible: Minimum age is 16 years.",
            "You are NOT eligible: Minimum UTME score is 200.",
            "You are NOT eligible: UNILAG must be your first choice.",
            "You are NOT eligible: Minimum of 5 credit passes required at one sitting.",
            "You are NOT eligible: Credit pass in English Language is required.",
            "You are NOT eligible: Credit pass in Mathematics is required.",
            "Invalid departmental cut-off mark. It must be between 200 and 320.",
            "You are NOT eligible: Your aggregate score does not meet the departmental cut-off."
        ]

        # Collect messages for any failed checks
        result = [msg for passed, msg in zip(checks, messages) if not passed]
        # Print the first failed message or a success message if all checks passed
        print(result[0] if result else "Congratulations! You are eligible for admission to UNILAG.")

    # Run the eligibility checker if the script is executed directly
if __name__ == "__main__":
        check_admission_eligibility()
        
        
        
"""
UNILAG Admission Eligibility Checker (2025/2026 Session)
This program checks a candidate's eligibility for admission into the University of Lagos (UNILAG) for the 2025/2026 academic session based on the following criteria:
1. Age Requirement: Candidate must be at least 16 years old.
2. UTME Score: Candidate must have a minimum UTME score of 200.
3. First Choice: UNILAG must be selected as the candidate's first choice institution.
4. O'Level Requirements: Candidate must have at least five (5) credit passes at one sitting, including English Language and Mathematics.
5. Post-UTME: Candidate must participate in the university's online Post-UTME screening and provide their score.
6. Departmental Cut-off: Candidate must meet the departmental cut-off mark (between 200 and 320), determined by the aggregate of UTME and Post-UTME scores.
The function prompts the user for all required details, checks each condition, and informs the user whether they are eligible for admission or not, providing specific feedback for unmet criteria.
"""