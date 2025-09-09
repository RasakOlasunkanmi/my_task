# List Methods
# Python provides many buitl-in methods to work with lists. Here is each method, what it does, and an example of how to use it.
#1. dot append() method
# Adds an element to the end of the list.
# fruits = ["apple", "banana"]
# fruits.append("cherry")
# print(fruits)    # Output: ['apple', 'banana', 'cherry']

#2. dot insert() method
# Inserts an element at a specified position in the list.
# fruits = ["apple", "banana"]
# fruits.insert(1, "orange")
# print(fruits)    # Output: ['apple', 'orange', 'banana']

#3. dot extend() method
# Adds elements from another iterable (like a list) to the end of the list.
fruits = ["apple", "banana"]
tropical = ["mango", "pineapple"]
fruits.extend(tropical)
print(fruits)    # Output: ['apple', 'banana', 'mango', 'pineapple']

#4. dot remove() method
# Removes the first occurrence of a specified value/element from the list.
fruits = ["apple", "banana", "cherry", "banana"]
fruits.remove("banana")
print(fruits)    # Output: ['apple', 'cherry', 'banana']

#5. dot pop() method
# Removes and returns the element at the specified position (or the last element if no index is specified). (default:last).
fruits = ["apple", "banana", "cherry"]
last_fruit = fruits.pop()
print(last_fruit)  # Output: 'cherry'
print(fruits)    # Output: ['apple', 'banana']

#6. dot clear() method
# Removes all elements from the list.
fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)    # Output: []

#7. dot index() method
# Returns the index of the first occurrence of a specified value/element in the list.
fruits = ["apple", "banana", "cherry"]
position = fruits.index("banana")
print(position)  # Output: 1

#8. dot count() method
# Counts how many times a value appears in the list.
fruits = ["apple", "banana", "cherry", "banana"]
print(fruits.count("banana"))  # Output: 2

#9. dot sort() method
# Sorts the list in ascending order by default. You can also specify the `reverse=True` argument to sort in descending order.
numbers = [3, 1, 4, 2]
numbers.sort()
print(numbers)  # Output: [1, 2, 3, 4]

# descending order
numbers.sort(reverse=True)
print(numbers)  # Output: [4, 3, 2, 1]

#10. dot reverse() method
# Reverses the order of the elements in the list.
fruits = ["apple", "banana", "cherry"]
fruits.reverse()
print(fruits)  # Output: ['cherry', 'banana', 'apple']

#11. dot copy() method
# Returns a shallow copy of the list.
fruits = ["apple", "banana", "cherry"]
new_list = fruits.copy()
print(new_list)    # Output: ['apple', 'banana', 'cherry']
