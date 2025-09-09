# Task5: Contact Quick Lookup
# - Store three names and their phone numbers in two separate tuples.
#   - Create a dictionary from them using `dict(zip(...))`.
#   - Ask the user for a name and display the corresponding number (or an error message).
# - Requirements:
#   - Use `zip()` and d`ict()` to combine tuples.
#   - Use `.get()` for safe retrieval.
#   - No loops.

# Method 1
names = ("Ade", "Bayo", "Deji")
nums = ("09012348709", "08154666980", "07087494048")
contacts = dict(zip(names, nums))

name = input("Enter a name: ").strip()
print(f"{name}'s number is {contacts[name]}")


# Method 2
names = ("Ade", "Bayo", "Deji")
nums = ("09012348709", "08154666980", "07087494048")
contacts = dict(zip(names, nums))
name = input("Enter a name: ")
number = contacts.get(name)
if number:
    print(f"{name}'s number is {number}")
else:
    print("Name not found.")