# Task1
# Step 1 - Write a program to take a string input from the user and display it in uppercase.
# Step 2 - Given the string "python", print its first and last characters.
# Step 3 - Ask the user for their name and print "Hello, <name>!" where <name> is the user’s input.
# Step 4 - Write a program to count the number of characters in a string without using len().
# Step 5 - Given "Hello World", replace "World" with "Python".

print(input("Enter a string: ").upper())

word = "python"
print(word[0],word[-1])

name = input("What is your name?: ")
print("Hello! where is the user's input?")
print(f"Oh! it is here {name}")

word = "Abiodun is a boy"
count = sum(1 for _ in word)
count = sum(1 for c in word if c != " ")
print("Number of characters (excluding spaces):", count)
print("Number of characters:", count)
print(word.index("o"))

text = "Hello, World"
print(text.replace("World", "Python"))