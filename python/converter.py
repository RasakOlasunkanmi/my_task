# TEMPERATURE CONVERTER

#Functions in Python:
#Defining functions for conversions

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def converter():
    print("============CONVERTER=========")

while True:
 print("======= Welcome to converter ========")
 print("Select conversion type:")
 print("\n1. Celsius to Fahrenheit")
 print("\n2. Fahrenheit to Celsius")
 print("\n3. Celsius to Kelvin")
 print("\n4. Kelvin to Celsius")
 print("\n5. Fahrenheit to Kelvin")
 print("\n6. Kelvin to Fahrenheit")
 print("\n7. End Converter")
 
 print("\n" + "=" * 45)
 choice = input("Enter choice (1-7): ")
 if choice == '7':
       print("\n" + "=" * 40)
       print("Thanks for using the Converter")
       print("\n" + "=" * 40)
       break
 
 try:
  temp = float(input("Enter temperature: "))
 
  if choice == '1':
        print("\n" + "=" * 45)
        print(f"Result: {celsius_to_fahrenheit(temp):.2f} F")
        print("Explanation: (Celsius * 1.8) / + 32")
  elif choice == '2':
        print("\n" + "=" * 45)
        print(f"Result:, {fahrenheit_to_celsius(temp):.2f} C")
        print("Explanation: (Fahrenheit - 32) * 5/9 .")
  elif choice == '3':
        print("\n" + "=" * 45)
        print(f"Result:, {celsius_to_kelvin(temp):.2f} K")
        print("Explanation: Celsius + 273.25 .")
  elif choice == '4':
        print("\n" + "=" * 45)
        print(f"Result:, {kelvin_to_celsius(temp):.2f} C")
        print("Explanation: Kelvin - 273.15 .")
  elif choice == '5':
        print("\n" + "=" * 45)
        print(f"Result:, {fahrenheit_to_kelvin(temp):.2f} K")
        print("Explanation: (Fahrenheit - 32) * 5/9 + 273.15 .")
  elif choice == '6':
        print("\n" + "=" * 45)
        print(f"Result:, {kelvin_to_fahrenheit(temp):.2f} F")
        print("Explanation: (Kelvin - 273.15) * 9/5 + 32 .")
  else:
        print("\n" + "=" * 45)
        print("Invalid choice!")
 except ValueError:
       print("Please enter a valid number for temperature.")
 continue_choice = input("\nDo you want to perform another convertion? (yes/no): ").strip().lower()
 if continue_choice not in ["yes", "y"]:
    print("\n" + "=" * 40)
    print("Thank you for using the Converter. Goodbye!") 
    break
 if __name__ == "__main__":
    converter()