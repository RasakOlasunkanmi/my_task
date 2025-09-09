
# Task2
# Step 1 - Check if a given string contains the substring "python" (case-insensitive).
# Step 2 - Write a program to reverse a string without using slicing ([::-1]).
# Step 3 - Given a string with extra spaces, remove the leading and trailing spaces.
# Step 4 - Ask the user to enter a sentence and print the number of vowels in it.
# Step 5 - Convert a string "1234" to an integer and multiply it by 2.

word = input("Enter a sentence: ")
sentence = word.lower()
text = "I love python as a programming language"

if "python" in text.lower():
    print("The string contains 'python'.")
else:
    print("The string does not contain 'python'.")

reversed_string = ""
for char in word:
    reversed_string = char + reversed_string
print("Reversed string:", reversed_string)

if word.strip() == word:
    print("No leading or trailing spaces.")
else:
    print("Spaces removed:", word.strip())

vowel_count = 0
for ch in sentence:
    if ch in "aeiou":
        vowel_count += 1
print("Number of vowels using control flow:", vowel_count)

char = "1234"

try:
    num = int(char)
    print("Double the integer:", num * 2)
except ValueError:
    print("Cannot convert to integer.")