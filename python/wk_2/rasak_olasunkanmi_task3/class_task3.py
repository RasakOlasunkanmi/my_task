# **Task1**

# 1. Write a program to take a string input from the user and display it in uppercase.

# 2. Given the string "python", print its first and last characters.

# 3. Ask the user for their name and print "Hello, <name>!" where <name> is the user’s input.

# 4. Write a program to count the number of characters in a string without using len().

# 5. Given "Hello World", replace "World" with "Python".

print(input("Enter a string: ").upper())

word = "python"
print(word[0],word[-1])

name = input("What is your name?: ")
print("Hello! where is the user's input?")
print(f"Oh! it is here {name}")

word = "Abiodun is a boy"
print(word.index("o"))

text = "Hello, World"
print(text.replace("World", "Python"))


# **Task2**

# 6. Check if a given string contains the substring "python" (case-insensitive).

# 7. Write a program to reverse a string without using slicing ([::-1]).

# 8. Given a string with extra spaces, remove the leading and trailing spaces.

# 9. Ask the user to enter a sentence and print the number of vowels in it.

# 10. Convert a string "1234" to an integer and multiply it by 2.

text = "I love python as a programming language"
print("python" in text)

word = "Good morning!"
reserved_string = " ".join(reversed(word))
print(reserved_string)

word = "  Abeokuta  "
print(word.strip())

word = input("Enter a sentence: ")
sentence = word.lower()
print("You have", sentence.count("a") + sentence.count("e") + sentence.count("i") + sentence.count("o") + sentence.count("u"), "vowels in the sentence.")

char = "1234"
print(int(char) * 2)


# **Task3: Pattern Matching & Splitting**
# 11. Given "apple,banana,orange", split the string into a list of fruits.

# 12. Ask the user for a sentence and print each word on a new line.

# 13. Replace all spaces in a string with underscores (_).

# 14. Count how many times the letter "a" appears in "Banana".

# 15. Check if a given string starts with "https://".

fruits = "apple,banana,orange"
print(fruits.split(",", 2))

sentence = input("Enter a sentence: ")
split_line = "\n".join(sentence.split())
print(split_line)

replace_name = "My name is Abiodun"
print(replace_name.replace(" ", "_"))

letter = "Banana"
print(letter.count("a"))

website = "https://www.winners.com"
print(website.startswith("https://"))