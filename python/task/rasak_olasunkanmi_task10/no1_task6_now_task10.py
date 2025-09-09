# Task1: Fruit collector
# - Ask the user to enter 5 favourite fruits. Store them in a set and display the set.

fruits = set()

try:
    for i in range(5):
        while True:  # keep asking until valid input
            fruit = input(f"Enter your favourite fruit {i + 1}: ")
            if fruit.strip():   # check that input is not empty
                fruits.add(fruit)
                break
            else:
                print("Fruit name cannot be empty. Please try again.")

    print("\nYour favourite fruits are:", fruits)

except Exception as e:
    print(f"Unexpected error: {e}")

finally:
    print("\tProgram finished")