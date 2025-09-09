# See Examples of use here

# range()
for i in range(3):
    print(i)     # 0, 1, 2

# zip()
names = ["Esther", "Precious", "Kennie"]
scores = [85, 90, 75]
for n, s in zip(names, scores):
    print(n, "scored", s)


# It's Ok, if you don't know what lambda is or how to use it. I will touch on it later. Just focus on the outputs
# map()
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, nums))
print(squared)     #[1, 4, 9, 16]


# filter()
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(even_nums)     # [2, 4]


# Student Performance & Feedback System

# Step 1: Input student data
name1 = input("Enter first student name: ")
score1 = int(input("Enter score for " + name1 + ": "))

name2 = input("Enter second student name: ")
score2 = int(input("Enter score for " + name2 + ": "))

name3 = input("Enter third student name: ")
score3 = int(input("Enter score for " + name3 + ": "))

# Step 2: Store in lists
names = [name1, name2, name3]
scores = [score1, score2, score3]

# Step 3: Display data
print("\nStudent Data:")
for index, (n, s) in enumerate(zip(names, scores)):
    print(f"{index + 1}. {n} - {s}")


# Step 4: Summary using built-ins
total = sum(scores)
average = round(total / len(scores), 2)
highest = max(scores)
lowest = min(scores)

print("\nPerformance Summary:")
print("Total Score:", total)
print("Average Score:", average)
print("Highest Score:", highest)
print("Lowest Score:", lowest)

# Step 5: Ranking (using sorted and zip)
ranked = sorted(zip(scores, names), reverse=True)
print("\nRanking:")
for rank, (score, name) in enumerate(ranked, 1):
    print(f"{rank}. {name} - {score}")


# Step 6: Check data types
print("\nData Type Checks:")
print("Type of names:", type(names))
print("Type of scores:", type(scores))
print("ID of names list:", id(names))
print("ID of scores list:", id(scores))


# Step 7: Filter passing students (>=50)
passing = list(filter(lambda s: s >= 50, scores))
print("\nPassing Scores:", passing)


# Step 8: Map names to uppercase
upper_names = list(map(lambda n: n.upper(), names))
print("Uppercase Names:", upper_names)

# Step 9: Use help() to show documentation of len
print("\nHelp on len():")
help(len)




# User Defined Function
# Defining a function
def greet():
    print("Hello, welcome to AI Fellowship!")

# When you want to use a function, this is how to call it.
# And you can call it as many times as possible.
greet()
greet()
greet()


# Function Arguments and Parameters

# Function with an argument - the placeholder
def greet(name):
    print("Hello", name, "welcome to Python learning!")

# Calling with parameter - the actual name
greet("Class rep")
greet("Ridwan")


# When to use return, print(), and yield keywords inside a function
#a. print()
#- You can use it if you are just interested in displaying your output (Not Storing). It does not give back a value you can use later.
#- Think of it like shouting information out loud, but not recording it for reference purpose.
#- So, you use it when you just want to slow results to the user. Example: printing menus, reports, or logs.

def greet(name):
    print("Hello", name)


# Function call
result = greet("Esther")

# You will notice that it did not store the name
print("Result:", result)

#b. return
#- You can use it if you want to give back a value.
#- return sends a value back to the function caller.
#- The function ends immediately once it hits return.
#- Think of it like filling a form and handing it back, the caller now owns the result and can reuse it.
#- So, you can use return when you need the result for further computation or storage. For example, math calculations, data processing, formatting text.

def add(a, b):
    return a + b

# Function call

result = add(4, 6)
print("The sum is:", result)

# Note the output and compare it with that of print()


#c. yield
#- This is used for producing a Sequence (Generators)
#- yield works like return, but instead of ending the function, it pauses it and remembers its state.
#- Next time you call it, it resumes from where it stopped.
#- This creates a generator.
#- You can use it when working with large data or infinite sequences.

def count_up_to(n):
    i = 1
    while i <= n:
        yield i    # pause and return i
        i += 1


# Using the generator
for number in count_up_to(5):
    print(number)

# Note the output: Instead of giving all numbers at once, the function yields them one at a time.

# More on Function Arguments(Types of Arguments)
#- Functions can accept different types of arguments depending on how we want to pass data. Understanding these makes functions flexible and powerful.
#1. Positional Arguments
#- These are the most common.
#- The order matters: values are assigned to parameters in the same order as they appear.
#- Think of it like lining up children in the same order as roll call.


def introduce(name, track):
    print("My name is", name)
    print("I am learning", track, ".")

# function call
introduce("Ngozi", "AI Engineering")     # Correct order

# change the arrangment and watch the output
introduce("AI Engineering", "Ngozi")    # Incorrect order, this will throw a semantic error


#2. Keyword Arguments
#- Here, you explicitly mention the parameter name when calling the function.
#- Order doesn't matter, since python knows which value goes where.
#- Think of it like addressing an envelope by name instead of position in line.

def introduce(name, track):
    print("My name is", name)
    print("I am learning", track,".")

# function call
introduce(name = "Ngozi", track = "AI Engineering")

# Change the arrangment and watch the output
introduce(track = "AI Engineering", name = "Ngozi")     #here you notice that order does not matter


#3. Default Arguments
#- Here, you can give parameters a default value.
#- Even if no value is provided when calling, the default is used.
#- Think of it like a restaurant menu where rice is served by default if you don't choose otherwise.

def introduce(name, track = "AI Engineering"):
    print("My name is", name)
    print("I am learning", track, ".")


# function call
# Without specifying the default argument, but watch the output
introduce("Paul")

# Specify the default argument and watch the output
introduce("Tunji Paul", track = "AI Development")


#4. Varying Length Arguments
#- Sometimes we don't know how many arguments will be passed. Python provides two special symbols (that is the asterisk)
#- Single asterisk for non-keyword arguments or tuple(*args)
#- Double asterisk for keyword argumnts or dictionary (**kwargs)


#a. non-keyword (tuple)
#- Collects extra positional arguments into a tuple
#- Think of it like packing extra clothes into a bag.

def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    print("Sum:", total)

# function call
# Total note of the output
add_numbers(2, 4, 6)
add_numbers(10, 20, 30, 40, 50)


#b. keyword argument (dictionary)
#- Collects extra keyword arguments into a dictionary.
#- Think of it like a labeled container where each item has a name tag.

def student_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)
        

# Lets implement on full code
# Define student profile function

# Ensure to not the order of arrangement of the types of arguments used.
# This is how to arrange it of you are using everything or some of the together.

def participant_profile(name, age, track="AI Development", *skills, **extra_info):
    """
    Generate a profile for a bootcamp participant using different types of arguments.
    """
    profile = f"\n--- Bootcamp Participant Profile ---\n"
    profile += f"Name: {name}\n"
    profile += f"Age: {age}\n"
    profile += f"Tracks: {track}\n"
    
    # Skills (from *args)
    if skills:
        profile += "Skills: " + ", ".join(skills) + "\n"
    else:
        profile += "Skills: Not yet specified\n"
        
    # Extra info (from **kwargs)
    if extra_info:
        profile += "Additional Info:\n"
        for key, value in extra_info.items():
            profile += f" - {key.capitalize()}: {value}\n"
            
    return profile   # Do you remember 'return' and why it is used? We are using it so it can be reused in other places.



# Example 1: Using only positional arguments
print(participant_profile("Peter", 24))


# Example 2: Adding keyword/default argument
print(participant_profile("Ridwan", 29, track="AI Engineering"))


# Example 3: Adding variable-length positional arguments (*args)
print(participant_profile("David", 27, "Data Science", "Python", "SQ", "Machine Learning"))


# Example 4: Adding variable-length keyword arguments (*args)
print(participant_profile(
    "Sophia", 30, "Cybersecurity",
    "Networking", "Ethical Hacking", "Python",
    interests="Blockchain", city="Shagamu", phone="08123456789"
))



"""Namespace
    - A namespace is like a "container" that holds names (variables, funcions, objects) and maps them to the actual stored in memory.
    - Think of it as a dictionary where keys are names and values are objects.
    - Python uses namespaces to avoid name conflicts.
    - Lets imagine a company where different departments can have employees with the same name:
    - a. In the IT department,there maybe a "Chris".
    - b. In the Training department, there may also be a "Chris".
    - Both exist, but they are identified by their department (namespace), so there's n confusion.
    
    Types of Namespace
    1. Built-in namespace - Provided by Python (e.g., len,print,list).
    2. Global namespace - Names defined at the top level of a script of module.
    3. Local namespace - Names created inside a function.
"""
    
    
# Global Namespace
employee = "General Employee"

def IT_department():
    # Local Namespace inside IT_department
    employee = "Chris (IT)"
    print("Inside IT Department:", employee)
    
def Training_department():
    # Local Namespace inside Training_department
    employee = "Chris (Training)"
    print("Inside Training Department:", employee)
    
print("In Global Namespace:", employee)     # Refers to global variable

IT_department()    # Uses local variable in IT
Training_department()    # Uses local variable in Training

# Using a built-in namespace function
print("Lenght of 'Python':", len("Python"))

# So, 'Chris' can exist in more than one namespace without confict.
# Please, take your timeto study the output carefully.

"""Scope
- Scope defines where in the code a name is accessible. Python follows the LEDB Rule (order of search for a variable):

L - Local >> Inside the current function.
E - Enclosing >> Inside any enclosing function(s).
G - Global >> At the top level of the script/module.
B - Built-in >> Python's built-in functions/objects
"""    

x = "global x"    # Global Namespace

def outer():
    x = "enclosing x"   # Enclosing Namespace
    
    def inner():
        x = "local x"   # Local Namespace
        print("Inside inner:", x)   # Local wins
        
    inner()
    print("Inside outer:", x)     # Enclosing
    
outer()
print("In global:", x)   # Global

# Watch the output
# Notice how Python searches in the order Local >> Enclosing >> Global >> Built-in (LEGB).


## Global keyword
# Used when you want to modify a global variable inside a function.

x = 5

def change_global():
    global x
    x = 10    # modifies the global x
    
change_global()
print(x)   # Output: 10


# nonlocal keyword
# Used in nested functions when you want to modify the variable from the enclosing scope (not global).

def outer():
    x = "outer x"
    
    def inner():
        nonlocal x
        x = "changed by inner"
        print("Inside inner:", x)
        
    inner()
    print("Inside outer:", x)

outer() 


# So understanding namespace and scope helps avoid name conflicts, makes modular code easier to read, and ensures functions and modules can work without interfering with each other.


""" Lambda Function

- A lambda function is a small, anonymous function (no name) defined using the lambda keyword.
- It can have any number of arguments, but only one expression.
- The result of the expression is automatically returned.
- This is the syntax
lambda arguments: expression

You use lambda;
1. When you need a short, throwaway function (not reuseable).
2. To avoid writing full def functions for small tasks.
3. Used with functions like map(), filter(), sorted(), and reduce().
"""


# Normal function
def square(x):
    return x ** 2

# Lambda function
square_lambda = lambda x: x ** 2

print(square(5))
print(square_lambda(5))

# Watch the output and note the difference

# This one has more than one arguments.

add = lambda a, b: a + b
print(add(3, 7))   # Output: 10


# Let us use lambda to apply the square function to a list

numbers = [1, 2, 3, 4] 
squares = list(map(lambda x: x**2, numbers))
print(squares)    # Output: [1, 4, 9, 16]


# Lets use lambda to sort the tuple within a list.
students = [("Ayo", 20), ("Bola", 18), ("Chika", 22)]
# Sort by age
sorted_students = sorted(students, key=lambda student: student[1])
print(sorted_students)


students_sorted_descending = sorted(students, key=lambda student: student[1], reverse=True)
print(students_sorted_descending)

students_sorted_alphabetically = sorted(students, key=lambda student:student[0])
print(students_sorted_alphabetically)