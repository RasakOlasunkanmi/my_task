# Task1: Your Favorite Life Quote
# Step 1 - Ask the user to input their favorite quote.
# Step 2 - Convert it to title case.
# Step 3 - Print it with quotation marks using escape sequences.

# Using loop

quote = input("Enter your favorite quote: ")
quote_title_case = quote.title()
if quote:
    print(f'Thank you for sharing your favorite quote: "{quote_title_case}"')
else:
    print("You did not enter a quote.")