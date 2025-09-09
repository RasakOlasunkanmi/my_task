
# Task 6: Word Analyzer
# Step 1 - Ask the user to input a word.
# Step 2 - Print the length of the word.
# Step 3 - Check if it is all uppercase, all lowercase, or title case.
# Step 4 - Reverse the word using slicing.

word = input("Enter a word: ")
print(f"Length of the word: {len(word)}")
if word.isupper():    
    print("The word is all uppercase.")
elif word.islower():
    print("The word is all lowercase.")   
elif word.istitle():
    print("The word is in title case.")
else:
    print("The word is in mixed case.")
reversed_word = word[::-1]
print(f"Reversed word: {reversed_word}") 