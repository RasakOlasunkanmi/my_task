# Task 3: Word Counter
# # Step 1 - Ask the user for a sentence.
# # Step 2 - Split the sentence into a list of words.
# # Step 3 - Print how many words are in the sentence.

# Using try-except-fianlly
try:
    sentence = input("Enter a sentence: ")
    
    if not sentence.strip():  # check if user entered only spaces or nothing
        raise ValueError("You must enter a sentence.")
    
    words = sentence.split()
    print(f"The sentence contains {len(words)} words.")

except ValueError as ve:
    print(f"Input Error: {ve}")
except Exception as e:
    print(f"Unexpected Error: {e}")
finally:
    print("\tProgram finished")