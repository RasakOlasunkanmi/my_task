# Python Modules
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


# Python Packages
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