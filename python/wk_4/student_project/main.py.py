# main.py >> Project entry point

# main.py

import data
import utils

# Add some students
data.add_student("Paul", "AI Engineering")
data.add_student("Blessing", "AI Development")

# Print formatted student records
for s in data.get_students():
    print(utils.format_student(s))