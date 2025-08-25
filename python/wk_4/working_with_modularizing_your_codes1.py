# # See Examples of use here

# # range()
# for i in range(3):
#     print(i)     # 0, 1, 2

# # zip()
# names = ["Esther", "Precious", "Kennie"]
# scores = [85, 90, 75]
# for n, s in zip(names, scores):
#     print(n, "scored", s)


# # It's Ok, if you don't know what lambda is or how to use it. I will touch on it later. Just focus on the outputs
# # map()
# nums = [1, 2, 3, 4]
# squared = list(map(lambda x: x**2, nums))
# print(squared)     #[1, 4, 9, 16]


# # filter()
# even_nums = list(filter(lambda x: x % 2 == 0, nums))
# print(even_nums)     # [2, 4]


# # Student Performance & Feedback System

# # Step 1: Input student data
# name1 = input("Enter first student name: ")
# score1 = int(input("Enter score for " + name1 + ": "))

# name2 = input("Enter second student name: ")
# score2 = int(input("Enter score for " + name2 + ": "))

# name3 = input("Enter third student name: ")
# score3 = int(input("Enter score for " + name3 + ": "))

# # Step 2: Store in lists
# names = [name1, name2, name3]
# scores = [score1, score2, score3]

# # Step 3: Display data
# print("\nStudent Data:")
# for index, (n, s) in enumerate(zip(names, scores)):
#     print(f"{index + 1}. {n} - {s}")


# # Step 4: Summary using built-ins
# total = sum(scores)
# average = round(total / len(scores), 2)
# highest = max(scores)
# lowest = min(scores)

# print("\nPerformance Summary:")
# print("Total Score:", total)
# print("Average Score:", average)
# print("Highest Score:", highest)
# print("Lowest Score:", lowest)

# # Step 5: Ranking (using sorted and zip)
# ranked = sorted(zip(scores, names), reverse=True)
# print("\nRanking:")
# for rank, (score, name) in enumerate(ranked, 1):
#     print(f"{rank}. {name} - {score}")


# # Step 6: Check data types
# print("\nData Type Checks:")
# print("Type of names:", type(names))
# print("Type of scores:", type(scores))
# print("ID of names list:", id(names))
# print("ID of scores list:", id(scores))


# # Step 7: Filter passing students (>=50)
# passing = list(filter(lambda s: s >= 50, scores))
# print("\nPassing Scores:", passing)


# # Step 8: Map names to uppercase
# upper_names = list(map(lambda n: n.upper(), names))
# print("Uppercase Names:", upper_names)

# # Step 9: Use help() to show documentation of len
# print("\nHelp on len():")
# help(len)




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
    print("I am learning", track".")


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