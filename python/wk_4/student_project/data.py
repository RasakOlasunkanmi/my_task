# data.py

students = []

def add_student(name, track):
    students.append({"name": name, "track": track})


def get_students():
    return students