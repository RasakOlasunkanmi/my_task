# upper()
# Converts all characters in the string to uppercase.
name = "Ada Balogun"
print(name.upper())  # ADA BALOGUN

# title()
# Converts all characters in the string to lowercase.
sentence = "python is amazing"
print(sentence.title())  # Python Is Amazing

# strip
# Removes whitespace (or specified characters) from both ends of the string.
text = "  Abuja  "
print(text.strip())  # Abuja

# replace()
# Replaces occurrences of a substring with another substring.
message = "I love Java"
print(message.replace("Java", "Python"))  # I love Python

# swapcase()
# Switches uppercase to lowercase and vice versa.
text = "Hello ABEOKUTA"
print(text.swapcase())  # hELLO abeokuta

# lstrip()
# Removes whitespace (or specified characters) from the left side only.
text = "  Nigeria"
print(text.lstrip())

# rstrip()
# Removes whitespace (or specified characters) from the right side only.
text = "Nigeria  "
print(text.rstrip())

# split()
# Splits a string into a list using a seperator (default is space).
fruits = "mango orange banana"
print(fruits.split())

# rsplit()
# Splits a string into a list from the right side.
text = "one,two,three,four"
print(text.rsplit(",", 2))
text = "one,two,three,four,five"
print(text.rsplit(',', 4))

# splitlines()
# Splits a string into a list at each newline (\n).
lines = "Line 1\nLine 2\nLine 3"
print(lines.splitlines())

# join()
# Joins a list of strings into a single string with a specified separator.
words = ["I", "love", "Python"]
print(" ".join(words))  # I love Python

# center()
# Centers the string within a specified width, padding with spaces or characters.
text = "Python"
print(text.center(20, '-'))  #  -------Python-------

# ljust()
# Left-justifies the string within a specified width, padding with spaces or characters.
text = "Python"
print(text.ljust(10, '-'))  # Python----

# rjust()
# Right-justifies the string within a specified width, padding with spaces or characters.
text = "Python"
print(text.rjust(10, '-'))  # ----Python  

# zfill()
# Pads a numeric on the left with until it reaches a given length.
num = "42"
print(num.zfill(5))  # 00042

# isalpha()
# Checks if the string contains only letters.
print("Lagos".isalpha())   # True
print("Lagos123".isalpha())  # False

# isdigit()
# Checks if the string contains only digits.
print("12345".isdigit())  # True
print("12345abc".isdigit())  # False

# isalnum()
# Checks if the string contains only letters and digits.
print("Python3".isalnum())  # True
print("Python 3".isalnum())  # False