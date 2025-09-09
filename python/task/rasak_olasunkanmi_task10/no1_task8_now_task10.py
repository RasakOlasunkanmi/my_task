min_age = 20  # Minimum age required for access

while True:
    user_input = input("Enter your age (or type 'exit' to quit): ")
    
    if user_input.strip().lower() == "exit":
        print("Exiting program...")
        break

    try:
        user_age = int(user_input)  # Try converting input to integer
        print(f"Access granted: {user_age >= min_age}")
    except ValueError:
        print("Invalid input. Please enter a valid number for age.")