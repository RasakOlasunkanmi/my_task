# Creating variables using str, int, and float
name = "Olasunkanmi"       # using str
print(name)
age = 30                   # using int
print(age)
height = 5.4               # using float
print(height)

# Type casting
# float()
# int()
# str()
# bool()

# Convert input to integer
age = int(input("Enter your age: "))
print(f"You will be {age + 1} years old nexyt year.")


# Calculator using input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
sum_result = num1 + num2
print(f"The sum of {num1} and {num2} is {sum_result}.")

# Using USSD code

# Step 1: Collect inputs
network = input("Enter your network: ")
amount = float(input("Enter amount: "))
send = input("Send: ")
cancel = input("Cancel: ")

# Step 2: Display inputs
print("Network:", network)
print("Amount:", amount)
print("Send option:", send)
print("Cancel option:", cancel)



# Simple USSD Simulation (no loops, no conditionals, no error handling)

# Step 1: Network selection
network = input("Enter your network: ")

# Step 2: Enter amount
amount = float(input("Enter amount: "))

# Step 3: Choose action
send = input("Type 'Send' to confirm: ")
cancel = input("Type 'Cancel' to abort: ")

# Step 4: Display transaction summary
print("\n--- USSD Transaction Summary ---")
print("Network:", network)
print("Amount:", amount)
print("Send option:", send)
print("Cancel option:", cancel)
print("Transaction Complete!" if send.lower() == "send" else "Transaction Cancelled")



# USSD Simulation with numbered menu (no loops, no conditionals, no error handling)

print("Welcome to MyBank USSD Service")
print("1. Airtime Purchase")
print("2. Data Purchase")
print("3. Check Balance")

# Step 1: Choose service
service = input("Enter the number of your choice: ")

# Step 2: Enter network
network = input("Enter your network: ")

# Step 3: Enter amount
amount = float(input("Enter amount: "))

# Step 4: Confirm or cancel
print("1. Send")
print("2. Cancel")
action = input("Enter your choice: ")

# Step 5: Display transaction summary
print("\n--- USSD Transaction Summary ---")
print("Service selected:", service)
print("Network:", network)
print("Amount:", amount)
print("Action:", action)
print("Transaction Complete!" if action == "1" else "Transaction Cancelled")



# Full USSD Simulation (linear, no loops, no conditionals)

print("Welcome to MyBank USSD Service")
print("1. Airtime Purchase")
print("2. Data Purchase")
print("3. Check Balance")

# Step 1: Choose service
service = input("Enter the number of your choice: ")

# Step 2: Network selection for Airtime or Data
network = input("Enter your network: ")

# Step 3: Amount entry for Airtime or Data
amount = float(input("Enter amount: "))

# Step 4: Confirmation menu
print("1. Send")
print("2. Cancel")
action = input("Enter your choice: ")

# Step 5: Display transaction summary
print("\n--- USSD Transaction Summary ---")
if service == "1":
    print("Service: Airtime Purchase")
elif service == "2":
    print("Service: Data Purchase")
else:
    print("Service: Balance Check")

print("Network:", network)
print("Amount:", amount)
print("Action:", action)
print("Transaction Complete!" if action == "1" else "Transaction Cancelled")