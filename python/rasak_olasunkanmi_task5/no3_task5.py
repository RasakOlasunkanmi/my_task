# Task3: Tuple Operations
# Step 1 - Create a tuple of 5 Nigerian states entered by the user.
# Step 2 - Print the first state and last state.
# Step 3 - Check if "Lagos" is in the tuple and print "Yes" or "No".
# Step 4 - Print the number of states entered.
# Step 5 - (Hint: use the tuple membership)

state1 = input("Enter Nigeria state: ").title()
state2 = input("Enter Nigeria state: ").title()
state3 = input("Enter Nigeria state: ").title()
state4 = input("Enter Nigeria state: ").title()
state5 = input("Enter Nigeria state: ").title()
Nigerian_states = (state1, state2, state3, state4, state5)
print("First state:", Nigerian_states[0])
print("Last state:", Nigerian_states[-1])
print("Lagos" in Nigerian_states)
print("Number of states entered:", len(Nigerian_states))