# Task 3: Word Counter
# Step 1 - Ask the user for a sentence.
# Step 2 - Split the sentence into a list of words.
# Step 3 - Print how many words are in the sentence.

# Using loop

sentence = input("Enter a sentence: ")

if sentence.strip():  # checks if the sentence is not empty or just spaces
    words = sentence.split()
    print(f"The sentence contains {len(words)} words.")
else:
    print("You did not enter a valid sentence.")