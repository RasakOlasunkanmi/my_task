# Task2: Unique Name Collector
#  - Write a program that collects the names of people attending a seminar (no duplicates allowed) and displays them in alphabetical order.

names = set()

for i in range(5):
    while True:
        try:
            name = input(f"Enter the name of person attending the seminar {i + 1}: ")
            if not name.strip():   # check if input is empty
                raise ValueError("Name cannot be empty. Please try again.")
            names.add(name)
            break   # valid input → break out of the loop
        except ValueError as e:
            print(e)
        finally:
            print("Input attempt completed.")  # runs whether valid or invalid

print(f"\nUnique names collected: {', '.join(sorted(names))}")