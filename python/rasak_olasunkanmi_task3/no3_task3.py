# Task3: Pattern Matching & Splitting
# Step 1 -  Given "apple,banana,orange", split the string into a list of fruits.
# Step 2 -  Ask the user for a sentence and print each word on a new line.
# Step 3 -  Replace all spaces in a string with underscores (_).
# Step 4 -  Count how many times the letter "a" appears in "Banana".
# Step 5 -  Check if a given string starts with "https://".

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