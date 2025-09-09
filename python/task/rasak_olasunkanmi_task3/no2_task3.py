# Task2
# Step 1 - Check if a given string contains the substring "python" (case-insensitive).
# Step 2 - Write a program to reverse a string without using slicing ([::-1]).
# Step 3 - Given a string with extra spaces, remove the leading and trailing spaces.
# Step 4 - Ask the user to enter a sentence and print the number of vowels in it.
# Step 5 - Convert a string "1234" to an integer and multiply it by 2.

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