##3 Python Modules
#1. Import the whole module

import math


# Lets put it to use

print(math.sqrt(9))
#- Note that you must specify the module name when calling a function within it.

#2. Import as an alias

import math as m

# Lets put it to use

print(m.sqrt(25))

#- This shortents the module name, this is common with libraries like numpy,pandas, etc.

#3. Import specific functions or variables

from math import sqrt, pi

print(sqrt(36))
print(pi)

#- Here you don't need the prefix 'math.' anymore


#4. Import everything from the module 

from math import *

print(sqrt(49))
print(pi)

#- This is usually not recommended because it can cause name conflicts if two modules have functions with the same name.

""" Writing Your Own Module
- Step1: Create a folder. Name it my_module
- Step2: Create a file inside the folder. Name it first.py
- Step3: Create another file inside the same folder. Name it second.py
- Step4: Create another file still inside the same folder. Name it main.py
"""


##4 Python Packages
"""
- What a package is (a folder with init.py)
- Installing and using third-party packages (pip install requests, import requests)
- Organizing multiple modules into a package

What is a Package?
- A package in Python is a way to organize related modules together into a folder.
- Inside this folder, there must be a special file called __init__.py (can be empty). This file tells Python that the folder should be treated as a package.
- uhmm, let think of a package as a standard mechanic workshop, and each module is a different toolbox inside the workshop. The init.py file is like the label on the workshop telling passerbys that this is a mechanic workshop.

Third-Party Packages
- Python comes with some built-in modules, but you can also install extra packages created by others.
These packages are stored in the Python Package Index (PyPI).
We install them using pip (Python's package manager) or conda a
"""


##5. Code Reusability

"""What is Code Reusability?

- Code reusability means writing code once and using it multiple times instead of rewriting it.

- It helps make programs cleaner, faster to develop, and easier to maintain.

- In Python, code reusability is achieved using;

    - Functions (reusing blocks of code)

    - Modules (saving functions in .py files to import later)

    - Packages (organizing modules in folders)

    - Classes & Objects (OOP makes reusable blueprints)

    - Libraries (built-in or third-party)


    
🔹 Why Reuse Code?

    - Saves time – no need to rewrite the same logic.

    - Avoids duplication – reduces errors from copy and paste.

    - Improves readability – your code is modular and organized.

    - Easy to maintain – update once, reuse everywhere.
"""


##6. Organizing a Python Project
"""- A modular project is a way of organizing your code into separate files and folders, each responsible for a specific task.
- This makes the project easier to read, test, and maintain.

Why Use Modular Structure?

- Separates concerns – Each file has one responsibility.

- Easier to debug – You can fix issues in one place without breaking others.

- Reusability – Functions/modules can be reused in other projects.

- Collaboration-friendly – Multiple developers can work on different parts.


**Folder & File Structure**

- Let’s say we want to build a Student Records Project.
- We will first structure our folder and files like this.
```
student_project/
│
├── data.py        # Handles storing and retrieving student data
├── utils.py       # Contains helper functions (e.g., calculations, formatting)
├── main.py        # Entry point to run the project

"""

"""
Let's Try A Bigger Project Structure
- As the project grow, we can organize into folders.

student_project/
│
├── my_data/                 # Data-related files
│   ├── __init__.py
│   └── data.py
│
├── my_utils/                # Helper functions
│   ├── __init__.py
│   └── utils.py
│
├── main.py               # Entry point
└── requirements.txt      # List of dependencies (if any)
"""


"""Lets work on Library Management System

- The goal of this project is to
 - Manage books in a library
 - Add books, list books, and borrow books.
 - Organized into folders and files for modularity.

 Lets structure the folder and possible files


library_project/
│
├── my_data/                   # Handles storage & retrieval
│   ├── __init__.py
│   └── data.py
│
├── utils/                  # Helper functions
│   ├── __init__.py
│   └── helpers.py
│
├── services/               # Core business logic
│   ├── __init__.py
│   └── library.py
│
├── main.py                 # Entry point of the program
└── requirements.txt        # (optional) external dependencies
""" 