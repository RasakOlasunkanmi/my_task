# Task2: Unique Name Collector
#  - Write a program that collects the names of people attending a seminar (no duplicates allowed) and displays them in alphabetical order.

names = set()

for i in range(5):
    name = input(f"Enter the name of person attending the seminar {i + 1}: ")
    names.add(name)   # set automatically removes duplicates

print(f"Unique names collected: {', '.join(sorted(names))}")