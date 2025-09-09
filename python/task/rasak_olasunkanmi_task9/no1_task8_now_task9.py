# Usecase 2: Access Control - Check if a user's age meets the minimum registration.

min_age = 20  # Minimum age required for access

while True:
    user_input = input("Enter your age (or type 'exit' to quit): ")
    if user_input.strip().lower() == "exit":
        print("Exiting program...")
        break

    user_age = int(user_input)  # Convert input to integer
    print(f"Access granted: {user_age >= min_age}")