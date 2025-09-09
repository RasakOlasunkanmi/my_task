# Task 6: Word Analyzer
# Step 1 - Ask the user to input a word.
# Step 2 - Print the length of the word.
# Step 3 - Check if it is all uppercase, all lowercase, or title case.
# Step 4 - Reverse the word using slicing.

try:
    word = input("Enter a word: ")

    if not word.strip():  # if input is empty or just spaces
        raise ValueError("You must enter a word.")

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

except ValueError as ve:
    print(f"Input Error: {ve}")
except Exception as e:
    print(f"Unexpected Error: {e}")
finally:
    print("\tProgram finished")