# Basic usage of input()
name = input("Enter your name: ")
print("Hello,", name)

# Convert input to integer
age = int(input("Enter your age: "))
print(f"You will be {age + 1} years old nexyt year.")

# Calculator using input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
sum_result = num1 + num2
print(f"The sum of {num1} and {num2} is {sum_result}.")

# Taking an order in Kentucky fried chicken
# Step1: Welcoming a customer
# Step2: Asking a customer wat he/she wants
# Step3: Displaying the customer's order
print("Welcome to Kentucky fried chicken")                           
customer_order = input("What will you like to order sir/ma?:")       
print(f"Here is your order: {customer_order}")                       

