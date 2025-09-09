# Data Structure Continued...2. List
# A list in Python is an ordered, mutable (changeable) collection that can store different types of data that is numbers, strings, booleans, even other lists.
# How to create a list
#* You can create an empty list when you don't have elements yet but plan to add later.
# Method 1: Using square brackets
empty_list = []
print(empty_list)    # Output: []

# Method 2: Using the list() constructor
empty_list2 = list()
print(empty_list2)   # Output: []

#** Creating a list with initial Elements.
# Lists can store multiple items seperated by commas inside square brackets.
# List of integers
numbers = [1, 2, 3, 4, 5]
print(numbers)   # Output: [1, 2, 3, 4, 5]

# List of strings
fruits = ["apple", "banana", "cherry"]
print(fruits)   # Output: ['apple', 'banana', 'cherry']

# Mixed data types
mixed_list = ["Alice", 25, 5.8, True]
print(mixed_list)   # Ouptput: ['Alice', 25, 5.8, True]

# *** Creating a List from another sequence. You can convert strings, tuples, or other iterables into a list.
# From a string (each character becomes an element)
chars = list("hello")
print(chars)    # Output: ['h', 'e', 'l', 'l', 'o']

# From a tuple...
# my_tuple = (10, 20, 30) list_from_tuple = list(my_tuple) print(list_from_tuple)#Output:[10, 20, 30]
# From a range...
# numbers_range = list(range(5)) print(numbers_range)# Output: [0, 1, 2, 3, 4]
# ****Creating a list using list comprehension. List comprehensions are a concise way to create lists using a loop in one line. We will come back to this later.
# Square of numbers 0-4
squares = [x**2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]

# Even numbers from 0-10
evens = [x for x in range(11) if x % 2 == 0]
print(evens)    # Output: [0, 2, 4, 6, 8, 10]

#***** Creating a Nested List. A list can contain other lists it is useful for matrices or grouped data.
# Matrix-like list
matrix = [[1, 2], [3, 4], [5, 6]]
print(matrix)  # Output: [[1, 2], [3, 4], [5, 6]]

# Accessing elements in a nested list
print(matrix[0])    # Output: [1, 2]
print(matrix[0][1]) # Output: 2

# Characteristics of a list
#1. Ordered collection
# The elements in a list maintain the order in which they are inserted.
# The first element has index 0, the second has index 1, and so on.
fruits = ["mango", "orange", "banana"]
print(fruits)   # Output: ['mango', 'orange', 'banana']
print(fruits[0])  # mango (first element)
print(fruits[1])  # orange (second element)
print(fruits[2])  # banana (third element)

#2. Allows duplicate
# Lists can stotre the same value multiple times.
items = ["rice", "beans", "yam", "rice"]
print(items)   # ['rice', 'beans', 'yam', 'rice']

#3. Mutable (can be chnaged)
# You can modify a list after it's created - change elements, add new ones, or remove existing ones.
numbers = [1, 2, 3]
numbers[1] = 20  # Changing element at index 1
print(numbers)   # [1, 20, 3]

#4. Can contain different data types
# A list can hold integers, strings, floats, booleans, and even other lists.
mixed = [10, "Nigeria", 3.14, True]
print(mixed)   # [10, 'Nigeria', 3.14, True]

#5. Can be Nested
# A list can contain other lists (2D or multi-dimensional lists).
nested_list = [[1, 2], ["a", "b"]]
print(nested_list)
print(nested_list[0][1])   # 2

#6. Dynamics size
# You don't need to declare the size of a list beforehand; it can grow or shrink as needed.
names = ["Ada"]
names.append("Bola")
names.append("Chidi")
print(names)   # ['Ada', 'Bola', 'Chidi']