# Simple Calculator Program

# Function to add two numbers
def add(a, b):
    return a + b

# Function to subtract second number from first
def subtract(a, b):
    return a - b

# Function to multiply two numbers
def multiply(a, b):
    return a * b

# Function to divide first number by second
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"
    
# Function to find square root of a number
def square_root(a):
    if a >= 0:
        return a ** 0.5
    else:
        return "Error: Negative input"
    
# Function for exponents
def exponential_power(a, b):
    if a >= 0 and b >= 0:
        return a ** b
    else:
        return "Error: Negative input"

# Display operation options to the user
def calculator():
    print("======CALCULATOR======")

while True:
 print("=====Welcome To Calculator=====")
 print("Select operation:")
 print("1. Add")
 print("2. Subtract")
 print("3. Multiply")
 print("4. Divide")
 print("5. Square Root")
 print("6. Exponents")
 print("7. Exit")

 # Take input from the user for operation choice
 print("=" * 40)
 choice = input("Enter choice (1/2/3/4/5/6/7): ").strip()
 if choice == '7':
       print("\n" + "=" * 40)
       print("Thanks for using the calculator")
       print("\n" + "=" * 40)
       break

 # Get two numbers as input from the user
 num1 = float(input("Enter first number: "))
 num2 = float(input("Enter second number: "))

 # Perform calculation based on user's choice :
 try :
    if choice == '1':
     print("\n" + "=" * 40)
     print("Result:", add(num1, num2))
    elif choice == '2':
     print("\n" + "=" * 40)
     print("Result:", subtract(num1, num2))
    elif choice == '3':
     print("\n" + "=" * 40)
     print("Result:", multiply(num1, num2))
    elif choice == '4':
     print("\n" + "=" * 40)
     print("Result:", divide(num1, num2))
    elif choice == '5':
     print("\n" + "=" * 40)
     print("Result:", square_root(num1))
    elif choice == '6':
     print("\n" + "=" * 40)
     print("Result:", exponential_power(num1, num2))
    else:
     print("\n" + "=" * 40)
     print("Invalid choice")
 except ValueError:
            print("\n" + "=" * 40)
            print("Error: Please enter valid numbers.")
 except OverflowError:
            print("\n" + "=" * 40)
            print("Error: Result is too large.")

 print("\n" + "=" * 40)
 continue_choice = input("\nDo you want to perform another calculation? (yes/no): ").strip().lower()
 if continue_choice not in ["yes", "y"]:
    print("\n" + "=" * 40)
    print("Thank you for using the calculator. Goodbye!") 
    break
 if __name__ == "__main__":
    calculator() 