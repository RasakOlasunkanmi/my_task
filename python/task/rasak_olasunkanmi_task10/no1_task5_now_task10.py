# Task1:  Create and Display

# Step 1 - Ask the user to enter three favorite Nigerian dishes (one at a time).
# Step 2 - Store them in a tuple called dishes.
# Step 3 - Print the tuple in a single line, separating items with commas.
# Step 4 - Use the \n escape sequence to print each dish on a new line.

try:
    dishes = ()

    for i in range(3):
        dish = input(f"Enter your favorite Nigerian dish {i + 1}: ")
        if not dish.strip():
            raise ValueError("Dish name cannot be empty.")
        dishes += (dish,)

    print("Your favorite Nigerian dishes are:")
    print(", ".join(dishes))   # all dishes in one line
    print("\n".join(dishes))   # each dish on a new line

except ValueError as ve:
    print(f"Input Error: {ve}")
except Exception as e:
    print(f"Unexpected Error: {e}")
finally:
    print("\tProgram finished")