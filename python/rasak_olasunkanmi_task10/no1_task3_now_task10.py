# Task1
# Step 1 - Write a program to take a string input from the user and display it in uppercase.
# Step 2 - Given the string "python", print its first and last characters.
# Step 3 - Ask the user for their name and print "Hello, <name>!" where <name> is the user’s input.
# Step 4 - Write a program to count the number of characters in a string without using len().
# Step 5 - Given "Hello World", replace "World" with "Python".

while True:
    try:
        print("\nChoose an option:")
        print("1. Convert input string to uppercase")
        print("2. Print first and last character of 'python'")
        print("3. Greet user by name")
        print("4. Find index of 'o' in 'Abiodun is a boy'")
        print("5. Replace 'World' with 'Python' in 'Hello, World'")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            print(input("Enter a string: ").upper())

        elif choice == "2":
            word = "python"
            print(word[0], word[-1])

        elif choice == "3":
            name = input("What is your name?: ")
            if not name.strip():
                raise ValueError("Name cannot be empty!")
            print(f"Hello, {name}!")

        elif choice == "4":
            word = "Abiodun is a boy"
            print(word.index("o"))  # if "o" not found, ValueError will be raised

        elif choice == "5":
            text = "Hello, World"
            print(text.replace("World", "Python"))
            
        elif choice == "6":
            word = "Abiodun is a boy"
            count = sum(1 for _ in word)
            print(count)

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

    except ValueError as ve:
        print(f"Value Error: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        print("\tEnd of operation")