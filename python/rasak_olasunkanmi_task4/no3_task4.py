# Task 3: Word Counter
# # Step 1 - Ask the user for a sentence.
# # Step 2 - Split the sentence into a list of words.
# # Step 3 - Print how many words are in the sentence.

sentence = input("Enter a sentence: ")
words = sentence.split()
print(f"The sentence contains {len(words)} words.")