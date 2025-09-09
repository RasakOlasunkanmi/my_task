# Task2 from wk_3 updated using loop 
# Step 1 - Check if a given string contains the substring "python" (case-insensitive).
# Step 2 - Write a program to reverse a string without using slicing ([::-1]).
# Step 3 - Given a string with extra spaces, remove the leading and trailing spaces.
# Step 4 - Ask the user to enter a sentence and print the number of vowels in it.
# Step 5 - Convert a string "1234" to an integer and multiply it by 2.

while True:
    print("\nString Operations\n")
    
    # Check if a word exists in text
    text = "I love python as a programming language"
    print("Is 'python' in text?", "python" in text)

    # Reverse a word
    word = "Good morning!"
    reversed_string = " ".join(reversed(word))
    print("Reversed word:", reversed_string)

    # Strip spaces
    word = "  Abeokuta  "
    print("Stripped word:", word.strip())

    # Count vowels in user input
    sentence = input("Enter a sentence (or type 'exit' to quit): ")
    if sentence.lower() == "exit":
        print("Exiting program...")
        break
    lower_sentence = sentence.lower()
    vowel_count = (
        lower_sentence.count("a") +
        lower_sentence.count("e") +
        lower_sentence.count("i") +
        lower_sentence.count("o") +
        lower_sentence.count("u")
    )
    print("Number of vowels in the sentence:", vowel_count)

    # Multiply numeric string
    char = "1234"
    print("Numeric string multiplied by 2:", int(char) * 2)
