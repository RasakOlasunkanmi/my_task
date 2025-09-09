# @title 13. Email Slicer(Extract Username from Email)

"""
Overview An Email Slicer is a simple yet useful tool that
extracts the username and domain from an email address.
This project enhances understanding of string manipulation,
user input handling, and string slicing in Python.
This project covers the step-by-step implementation of an
Email Slicer, including handling user input, extracting the
username and domain, and displaying the results.

Key Concepts of Email Slicer in Python

String Manipulation:

- Using string methods like split() and
- Extracting specific parts of a string

User Input Handling:

- Accepting an email address from the user
- Validating the input format

Output Formatting:

- Displaying extracted username and domain clearly
"""



"""Hands-On Exercise

Try improving the Email Slicer with
these additional features:

1. Allow case-insensitive input handling.
2. Validate email using regex for stricter format
checking.
3. Provide domain categorization, such as
personal or corporate emails.
4. Create a GUI version using Streamlit for better
user experience.
5. Enhance output formatting with additional
user details.
"""


import re


def validate_email(email):
    # Define a stricter regex for email validation
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(regex, email):
        return True
    return False

def email_slicer(email):
    if "@" in email and '.' in email.split('@')[1]:
        username, domain = email.split('@')
        return username, domain
    else:
        return None, None
    
email = input("Enter your email address: ").strip().casefold()
username, domain = email_slicer(email)

# Display the result
if username and domain:
    print(f"Username: {username}\nDomain: {domain}")
else:
    print("Invalid email format! Please enter a valid email.")


# Define personal and corporate domain patterns
personal_domains = ["gmail.com", "yahoo.com", "hotmail.com"]
corporate_domains = ["company.com", "organization.org", "corporate.co"]
emails = personal_domains, corporate_domains

# Function to categorize emails
def categorize_email(email):
    domain = email.split("@")[-1]
    if domain in personal_domains:
        return "Personal"
    elif domain in corporate_domains:
        return "Corporate"
    else:
        return "Unknown"

# Categorize each email
categorized_emails = {email: categorize_email(email) for email in emails}





try:
    # Define personal and corporate domain patterns
    personal_domains = ["gmail.com", "yahoo.com", "hotmail.com"]
    corporate_domains = ["company.com", "organization.org", "corporate.co"]
    emails = personal_domains, corporate_domains

    # Function to categorize emails
    def categorize_email(email):
        domain = email.split("@")[-1]
        if domain in personal_domains:
            return "Personal"
        elif domain in corporate_domains:
            return "Corporate"
        else:
            return "Unknown"

    # Function to slice the email into username and domain
    def email_slicer(email):
        # Check if the email contains "@" and "." in the domain part
        if "@" in email and '.' in email.split('@')[1]:
            # Split the email into username and domain
            username, domain = email.split('@')
            return username, domain
        else:
            # Return unknown if the email format is invalid
            return "Unknown"

    # Get email input from the user
    email = input("Enter your email address: ").casefold()

    # Call the function to slice the email
    username, domain = email_slicer(email)

    # Display the result
    if username and domain:
        print(f"Username: {username}\nDomain: {domain}")
    else:
        print("Invalid email format! Please enter a valid email.")
except ValueError:
    print("Invalid email address.")