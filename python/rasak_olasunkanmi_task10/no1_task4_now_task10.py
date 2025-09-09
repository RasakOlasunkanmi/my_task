 # Using try-except-finally   
try:
    quote = input("Enter your favorite quote: ")
    quote_title_case = quote.title()

    if quote:
        print(f'Thank you for sharing your favorite quote: "{quote_title_case}"')
    else:
        print("You did not enter a quote.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")

finally:
    print("\tProgram finished")