# List Operations in Python
# Python lists support a variety of operations for creating, modifying, and working with data. We will go through them step by step now.
#1. Concatenation (+)
# Joins two lists into a new list.

list1 = [1, 2, 3]
list2 = [4, 5]
result = list1 + list2
print(result)   # [1, 2, 3, 4, 5]

#2. Repetition (*)
# Repeats elements in a list a given number of times.
nums = [1, 2]
repeated = nums * 3
print(repeated)   # [1, 2, 1, 2, 1, 2]

#3. Indexing
# Accessing elements using their position (starting from 0).
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # apple
print(fruits[-1]) # cherry (negatives index starts from the end)

#4. Slicing
# Extract a portion of the list.
numbers = [0, 1, 2, 3, 4, 5]
print(numbers[1:4])  # [1, 2, 3]
print(numbers[:3])   # [0,1,2]
print(numbers[3:])   # [3, 4, 5]
print(numbers[::2])  # [0, 2, 4] (step of 2)

#5. Membership (in/not in)
# Checks if an element exists in a list.
colors = ["red", "green", "blue"]
print("green" in colors)   # True
print("yellow" not in colors)  # True

#6. Length (len())
# Counts the number of elements in a list.
items = ["pen", "book", "laptop"]
print(len(items))   # 3

#7. Min and Max (min()/ max())
# Returns the smallest or largest elemets.
nums = [5, 2, 9, 1]
print(min(nums))   # 1
print(max(nums))   # 9

#8. Sum (sum())
# Adds all numerical elements in a list.
numbers = [1, 2, 3, 4]
print(sum(numbers))   # 10

#9. List comprehension
# Creates a list in a single line.
squares = [x**2 for x in range(5)]
print(squares)   # [0, 1, 4, 9, 16]

#10. Copying a list
# create a dupliacte list.
a = [1, 2, 3]
b = a.copy()  # or b = list(a)
print(b)  # [1, 2, 3]