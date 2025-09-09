# Task 7: List Manipulation
# Step 1 - Create a list of five cities.
# Step 2 - Replace the third city with a new one (entered by the user).
# Step 3 - Remove the last city.
# Step 4 - Add a new city to the beginning of the list.
# Step 5 - Print the updated list.

cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
new_city = input("Enter a new city to replace the third city: ")
cities[2] = new_city # Replace the third city
cities.pop()  # Remove the last city
cities.insert(0, "San Francisco") # Add a new city to the beginning
print("Updated list of cities: ") 