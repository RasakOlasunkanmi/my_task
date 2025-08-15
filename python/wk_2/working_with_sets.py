# Sets in Pyhton
# In Python, a set is an unordered collection of unique elements. Sets are useful when you want to store multiple items but avoid duplicates.
# Creating Sets
#1. Using curly braces:
fruits = {"apple", "banana", "mango"}
print(fruits)     # Or
print("Fruits set:", fruits)

#2. Using the set() constructor:
numbers = set([1, 2, 3, 4])
print(numbers)    # Or
print("Numbers set:", numbers)

#3. Creating an empty set (must use set(), not {}):
empty_set = set()
print(empty_set)    

#4. From a string (duplicates removed automatically):
letters = set("mississippi")
print(letters)    # Or
print("Letters set:", letters)


# Characteristics of Sets
#1. Unordered: No defined indexing or sequence.
#2. Unique elements: Duplicates are automatically removed.
#3. Mutable: You can add or remove elements/items.
#4. Unindexed: You cannot access elements by index like lists or tuples (e.g., my_set[0]).
#5. Supports mathematical set operations: Union, Intersection, Difference, Symmetric difference.


# Set Operations
#1. Adding Elements
colors = {"red", "blue"}
colors.add("green")
print(colors)  # Output: {'red', 'blue', 'green'}

#2. Removing Elements
colors.remove("blue")  # Remove an element, raises error if not found
colors.discard("yellow")  # Remove an element, does not raise error if not found
print(colors)

#3. Pop an element (removes and returns an arbitrary element):
colors = {"red", "blue", "green"}
removed = colors.pop()
print("Removed:", removed)
print("Remaining:", colors)

#4. Clear a Set
colors.clear()  # Removes all elements
print(colors)  # Output: set()

##. Mathematical Set Operations

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

#1. Union
print(set1 | set2) # Output: {1, 2, 3, 4, 5, 6}
print(set1.union(set2))  # Output: {1, 2, 3, 4, 5, 6}

#2. Intersection
print(set1 & set2)  # Output: {3, 4}
print(set1.intersection(set2))  # Output: {3, 4}

#3. Difference
print(set1 - set2)  # Output: {1, 2}
print(set1.difference(set2))  # Output: {1, 2}

#4. Symmetric Difference
print(set1 ^ set2)
print(set1.symmetric_difference(set2))  # Output: {1, 2, 5, 6}

### Working with Sets
# Collecting unique visitors to an event
visitors = set()

# Adding visitors
visitors.add("Alice")
visitors.add("Bob")
visitors.add("Charlie")
visitors.add("Alice")  # Duplicate, will not be added(ignored automatically)
print("Visitors:", visitors)

# Checking if a visitor attended
# (Don't worry if you can't figure this part out yet, we will discuss it properly later in the course.)
# if "Alice" in visitors:
#     print("Alice attended the event.")
# ("Bob" in visitors)  # Returns True
# ("David" in visitors)  # Returns False   

name = "Aisha"
if name in visitors:
    print(f"{name} attended the event.")
else:
    print(f"{name} did not attend the event.")