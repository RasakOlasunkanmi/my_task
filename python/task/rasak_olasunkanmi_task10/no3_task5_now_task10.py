# Task3: Tuple Operations
# Step 1 - Create a tuple of 5 Nigerian states entered by the user.
# Step 2 - Print the first state and last state.
# Step 3 - Check if "Lagos" is in the tuple and print "Yes" or "No".
# Step 4 - Print the number of states entered.
# Step 5 - (Hint: use the tuple membership)

try:
    Nigerian_states = ()

    for i in range(5):
        state = input(f"Enter the name of Nigerian state in title case {i + 1}: ")
        if not state.strip():   # check for empty input
            raise ValueError("State name cannot be empty.")
        Nigerian_states += (state,)

    print("First state:", Nigerian_states[0])
    print("Last state:", Nigerian_states[-1])
    print("Lagos" in Nigerian_states)
    print("Number of states entered:", len(Nigerian_states))

except ValueError as ve:
    print(f"Input Error: {ve}")
except Exception as e:
    print(f"Unexpected Error: {e}")
finally:
    print("\tProgram finished")