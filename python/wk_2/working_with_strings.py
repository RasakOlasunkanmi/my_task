# Single quotes
name = 'Ada'
print(name)

# Double quotes
greeting = "Hello"
print(greeting)

# Tripple quotes (for multi-line strings)
story = '''Once upon a time, there was a coder named Ada.'''
print(story)

# String with numbers and symbols
password = "p@ssword123"
print(password)

# String operations
# Indexing
word = "Python"
print(word[0])   # P
print(word[-1])  # n

word = "Good morning World"
print(word[0])
print(word[5])
print(word[-1])
print(word[-5])

# Slicing
word = "Python"
print(word[0:4])  # Pyth
print(word[2:])   # thon
print(word[:3])   # Pyt
print(word[-3:])  # hon
print(word[::-5]) # nohtyP (reversed)

# String Concatenation & Repetition
# Concatenation
a = "Hello"
b = "World"
print(a + " " +b)  # Hello World

# Repetition
word = "Hi! "
print(word * 3)  # Hi! Hi! Hi!

# String Searching & Checking
# Membership
text = "Python programming"
print("Python" in text)  # True
print("Java" not in text)  # True

# find() / rfind()
text = "Hello World"
print(text.find("o"))  # 4
print(text.rfind("o"))  # 7

# index() / rindex()
# (Like find() but raises an error if not found)
text = "Hello World"
print(text.index("World"))  # 6

# startswith() / endswith()
filename = "data.csv"
print(filename.startswith("data"))  # True
print(filename.endswith(".csv"))  # True

sentence = "My name is Adegoroye Oladiran Abiodun, I am in 400l in the department of Computer Science at the University of Lagos."
print(sentence[:47])
print(sentence[1:30:2])  # Slicing with step
print(sentence[::3])    # Slicing with step
print(sentence[::-1])  # Reversed string
print(sentence[47:])    
print(sentence[47:100])  # Slicing beyond string length
print(sentence[100:])
print(sentence[100:200])  # Slicing beyond string length
print(sentence[::]) 
print(sentence.find("i"))
print(sentence.rfind("i"))  # Last occurrence of 'i'
print(sentence.index("400l"))
print(sentence.rindex("400l"))  # Last occurrence of '400l'
print(sentence.startswith("My name"))