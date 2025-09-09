# Task5: Contact Quick Lookup
# - Store three names and their phone numbers in two separate tuples.
#   - Create a dictionary from them using `dict(zip(...))`.
#   - Ask the user for a name and display the corresponding number (or an error message).
# - Requirements:
#   - Use `zip()` and d`ict()` to combine tuples.
#   - Use `.get()` for safe retrieval.
#   - with error handling.

names = ("Ade", "Bayo", "Deji")
nums = ("09012348709", "08154666980", "07087494048")
contacts = dict(zip(names, nums))

try:
    name = input("Enter a name: ").strip()  # remove accidental spaces
    number = contacts.get(name)

    if number:
        print(f"{name}'s number is {number}")
    else:
        raise KeyError(f"'{name}' not found in contacts.")

except KeyError as e:
    print("Error:", e)

except Exception as e:
    print("An unexpected error occurred:", e)

finally:
    print("\nSearch finished.")