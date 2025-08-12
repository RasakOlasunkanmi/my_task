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

# Using ussd code
# Step1: 
network = input("Enter your network: ")
amount = float(input("Enter amount: "))
send = str(input("send: "))
cancel = str(input("cancel: "))
print(cancel)