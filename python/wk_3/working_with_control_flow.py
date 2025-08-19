# Control Flow in Python
# Control flow refers to the order in which statements are executed in a program. Instead of always running line by line, control flow allows your program to:
# - Make decisions (choose one path or another, explore alternatives)
# - Repeat actions (loops)
# - Exit or skip parts of code 
# It is the foundation for logic and problem solving in programming
# Control flow is divided into 3 parts

# A. Conditional Statements
#1. if Statement
# Executes a block only when a condition is true.

age = 20
if age >= 18:
    print("You are eligible to vote")  # Output: You are eligible to vote

# Some usecases
#1 Checking for eligibility
#2 Validating login attempts
#3 Ensuring a minimum purchase requirement, etc

#2. if-else Statement
# - Provides two alternatives paths.

wallet = 400
price = 500

if wallet >= price:
    print("Purchase successful")
else:
    print("Insufficient balance")      # Output: Insufficient balance

# Some usecases
# 1. Deciding success or failure ofn payment
# 2. Granting or denying access to a system
# 3. Determining pass/fail in an exam, etc

#3. if-elif-else Statement
# Used for multiple conditions

score = 85
if score >= 70:
    print("Grade A")
elif score >= 50:
    print("Grade B")
else:
    print("Grade C")    # Output: Grade A

# Some usecases
#1. Student grading systems
#2. Assigning ticket categories (VIP, Regular, Student)
#3. Categorizing temperatures (Hot, Warm, Cold), etc

#4. Nested if
# Placing an if inside another if.

age = 19
citizen = True

if age >= 18:
    if citizen:
        print("You can vote")
    else:
        print("You must be a citizen to vote")
else:
    print("Too young to vote")   # Output: You can vote


# Some usecases
#1. Voting eligibility (age + citizen)
#2. Banking (account active + balance sufficient)
#3. School admission (age + grade level)


# B. Loops
#1. for loop
# This is used for iterating over a sequence (strings, list, tuple, dictionary)

# Iterates through each element in a LIST.

fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"I like {fruit}")    #I like apple  # I like banana  # I like orange


# Some usecases
# Iterating through shopping lists
# Checking availability of products
# Displaying student names, etc

# Iterates through each element in a TUPLE. This works like lists, but remember that tuples are immutable.

coordinates = (0.34654, -0.48585, 0.57477)
for point in coordinates:
    print(f"Point: {point}")     # Output: Point: 0.34654  Point: -0.48585  Point: 0.57477


# Some usecases
# Storing fixed sensor readings
# Displaying fixed seating positions, etc


# Iterates through each element in a DICTIONARY. Remember that dictionaries have key-value pairs.

student = {"name": "Tunde", "age": 16, "grade": "A"}
for key, value in student.items():
    print(f"{key}: {value}")    # Output: name: Tunde  age: 16  grade: A


# Iterates through each element in a STRING. Remember that strings are sequence of characters.

word = "PYTHON"
for char in word:
    print(char)

# Some usecases 
# - Counting vowels/consonants
# - Password validation (checking digits/speecial chars)
# - Text analysis, etc


#2. While loop
# A while loop is used to repeatedly execute a block of code as long as a given condition is true. Unlike the for loop (which iterates over sequences like lists, tuples, etc), the while loop is condition-based

# while condition:
    # code block
# The condition must evaluate to True for the loop to continue running
# When the condition becomes False, the loop stops.

# Using while loop

## Documenting my thoughts
#- Let the loop start with count = 1
#- Let it keep printing until count is greater than 5
#- Let the loop terminate when the condition is no longer true

## My code
count = 1
while count <= 5:
    print("Number:", count)
    count += 1       # Number: 1 Number: 2 Number: 3 Number: 4 Number: 5


# Incrementing with 'while'

num = 1
while num <= 10:
    print(num, end=" ")
    num += 1         # Output: 1 2 3 4 5 6 7 8 9 10 


# Decrementing with 'while'

timer = 10
while timer > 0:
    print("Countdown:", timer)
    timer -= 1


# While with User Input
## Keep asking until the user enters a correct password.

password = ""
while password != "python123":
    password = input("Enter the password: ")

print("Access Granted!")


# Understanding while True
#- The while True: loop is an infinite loop - it keeps running forever until you explicity stop it with a break statement or by exiting the program.
#- It is commonly used when:
#-- You don't know in advance how many times you want the loop to run.
#-- You want to keep asking the user for input until a valid condition is met.
#-- You are building continous programs like menus, login systems, or simulations.

# while True:
    # Code block
    # Must include a break statement to stop

