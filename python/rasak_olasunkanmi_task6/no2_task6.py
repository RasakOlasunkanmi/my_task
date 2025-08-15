# Task2: Unique Name Collector
#  - Write a program that collects the names of people attending a seminar (no duplicates allowed) and displays them in alphabetical order.

name1 = input("Enter the name of a person attending the seminar: ")
name2 = input("Enter the name of a person attending the seminar: ")
name3 = input("Enter the name of a person attending the seminar: ")
name4 = input("Enter the name of a person attending the seminar: ")
name5 = input("Enter the name of a person attending the seminar: ")
names = {name1, name2, name3, name4, name5}
print(f"Unique names collected: {', '.join(sorted(names))}")

