# Task4: Unique Members Registration
# - Ask the user to enter three names separated by commas.
#    - Convert them to a set to ensure uniqueness.
#    - Create a dictionary where each name is a key and its length is the value.
# - Requirements:
#    - Use `.split(",")` and `set()` to remove duplicates.
#    - Use dictionary comprehension `{name: len(name) for name in set_of_names}`.

# Method 1
name1 = input("Enter name (seperated by comma):" )
name2 = input("Enter name (seperated by comma):" )
name3 = input("Enter name (seperated by comma):" )
names = {name1, name2, name3}
names_input = ",".join([name1, name2, name3])
unique_names = set(n.strip() for n in names_input.split(",") if n.strip())
name_length_dict_alt = {name: len(name) for name in unique_names}
print(name_length_dict_alt)


# Method 2
name1 = input("Enter name (seperated by comma):" )
name2 = input("Enter name (seperated by comma):" )
name3 = input("Enter name (seperated by comma):" )
names = {name1, name2, name3}
set_of_names = set()
for name_list in names:
    set_of_names.update(n.strip() for n in name_list.split(",") if n.strip())
name_length_dict = {name: len(name) for name in set_of_names}
print(name_length_dict)