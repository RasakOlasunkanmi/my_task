import math

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
    
# Function for modulus
def modulus(a, b):
    if b != 0:
        return a % b
    else:
        return "Error: Modulus by Zero"
    
# Function for factorial
def factorial(n):
    if n < 0:
        return "Error: Negative input for factorial"
    elif n != int(n):
        return "Error: Factorial only works for integers"
    else:
        return math.factorial(int(n))

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
    print("7. Modulus")
    print("8. Factorial")
    print("9. Exit")

    # Take input from the user for operation choice
    print("=" * 40)
    choice = input("Enter choice (1/2/3/4/5/6/7/8/9): ").strip()
    if choice == '9':
        print("\n" + "=" * 40)
        print("Thanks for using the calculator")
        print("\n" + "=" * 40)
        break

    # Perform calculation based on user's choice :
    try:
        if choice == '5': # Square Root (one number)
            num1 = float(input("Enter the number: "))
            print("\nResult:", square_root(num1))

        elif choice == '8':  # Factorial (one number, integer only)
            num1 = float(input("Enter the number: "))
            print(f"Number entered: {num1}!")
            print("\nResult:", factorial(num1))

        elif choice in ['1', '2', '3', '4', '6', '7']:  # Two-number operations
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        
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
            elif choice == '6':
                print("\n" + "=" * 40)
                print("Result:", exponential_power(num1, num2))
            elif choice == '7':
                print("\n" + "=" * 40)
                print("\nResult:", modulus(num1, num2))
        else:
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