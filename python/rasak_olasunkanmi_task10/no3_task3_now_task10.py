# Using Error handling    
try:
    # User input for fruits
    fruits = input("Enter fruits separated by commas: ")
    
    # Split into a list
    fruit_list = fruits.split(",")
    
    # Check if "banana" is in the list
    if "banana" in fruit_list:
        print("Banana is in the list of fruits.")
    else:
        print("Banana is not in the list of fruits.")

except Exception as e:
    print("An error occurred:", e)