# **Task1: Your Favorite Life Quote**
# - Ask the user to input their favorite quote.

# - Convert it to title case.

# - Print it with quotation marks using escape sequences.

# quote = input("Enter your favorite quote: ")
# quote_title_case = quote.title()
# print(f'"{quote_title_case}"')

# **Task 2: Shopping List Manager**
# - Create an empty list.

# - Ask the user to enter 3 shopping items (one by one).

# - Add them to the list.

# - Display the list as a single string, separated by commas.

# shopping_list = []
# for i in range(3):
#     item = input(f"Enter shopping item {i + 1}: ")
#     shopping_list.append(item)
# print("Shopping List: " + ", ".join(shopping_list))

# Item_1 = input("Enter your shopping item1: ")
# Item_2 = input("Enter your shopping item2: ")
# Item_3 = input("Enter your shopping item3: ")
# shopping_list = [Item_1, Item_2, Item_3]
# print("Shopping List: " + ", ".join(shopping_list))

# **Task 3: Word Counter**
# - Ask the user for a sentence.

# - Split the sentence into a list of words.

# - Print how many words are in the sentence.

# sentence = input("Enter a sentence: ")
# words = sentence.split()
# print(f"The sentence contains {len(words)} words.")

# **Task 4: Name Organizer**
# - Ask the user to enter 5 names (separated by spaces).

# - Convert all names to lowercase.

# - Sort the list alphabetically.

# - Display them one name per line.
#   -Tips: use `range()`,`sort()`, `for`, `in`, `split()`, `len()`,`lower()` 

# names_input = input("Enter 5 names separated by spaces: ")
# names_list = names_input.split(",")
# names_list = [name.lower() for name in names_list]
# names_list.sort()
# for i in range(len(names_list)):
#     print(names_list[i])

# **Task 5: Student Score Tracker**

# - Ask the user for 3 student names.

# - For each student, ask for their score.

# - Store the results in two lists (one for names, one for scores).

# - Print a formatted output showing Name — Score, aligned neatly.
#   - Tips: You are to start by creating two empty lists.
# names = []
# scores = []
# print("Enter the names and scores of 3 students:")
# for i in range(3):
#     name = input(f"Enter name of student {i + 1}: ")
#     score = input(f"Enter score for {name}: ")
#     names.append(name)
#     scores.append(score)
# print("\nStudent Scores:")
# for i in range(len(names)):
#     print(f"{names[i]:<20} — {scores[i]}")

# **Task 6: Word Analyzer**
# - Ask the user to input a word.

# - Print the length of the word.

# - Check if it is all uppercase, all lowercase, or title case.

# - Reverse the word using slicing.
# word = input("Enter a word: ")
# print(f"Length of the word: {len(word)}")
# if word.isupper():    
#     print("The word is all uppercase.")
# elif word.islower():
#     print("The word is all lowercase.")   
# elif word.istitle():
#     print("The word is in title case.")
# else:
#     print("The word is in mixed case.")
# reversed_word = word[::-1]
# print(f"Reversed word: {reversed_word}") 

# **Task 7: List Manipulation**
# - Create a list of five cities.

# - Replace the third city with a new one (entered by the user).

# - Remove the last city.

# - Add a new city to the beginning of the list.

# # - Print the updated list.
# cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
# new_city = input("Enter a new city to replace the third city: ")
# cities[2] = new_city # Replace the third city
# cities.pop()  # Remove the last city
# cities.insert(0, "San Francisco") # Add a new city to the beginning
# print("Updated list of cities:")    