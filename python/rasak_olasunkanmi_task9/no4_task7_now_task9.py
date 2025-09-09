# Task4: Unique Members Registration
# - Ask the user to enter three names separated by commas.
#    - Convert them to a set to ensure uniqueness.
#    - Create a dictionary where each name is a key and its length is the value.
# - Requirements:
#    - Use `.split(",")` and `set()` to remove duplicates.
#    - Use dictionary comprehension `{name: len(name) for name in set_of_names}`.

set_of_names = set()

for i in range(3):  # loop for 3 inputs
    name_list = input(f"Enter name(s) {i+1} (separated by commas): ")
    set_of_names.update(n.strip() for n in name_list.split(",") if n.strip())

name_length_dict = {name: len(name) for name in set_of_names}

print("\nName and Length Dictionary:")
print(name_length_dict)