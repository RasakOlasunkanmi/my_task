# Task1: Fruit collector
# - Ask the user to enter 5 favourite fruits. Store them in a set and display the set.

fruits = set()

for i in range(5):
    fruit = input(f"Enter your favourite fruit {i + 1}: ")
    fruits.add(fruit)

print("Your favourite fruits are:", fruits)