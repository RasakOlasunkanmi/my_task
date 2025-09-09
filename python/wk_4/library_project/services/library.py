# services/library.py - This will handle business logic

import my_data.data as data

def borrow_book(title):
    for book in data.get_books():
        if book["title"].lower() == title.lower() and book["available"]:
            book["available"] = False
            return f"You have borrowed '{book['title']}'"
    return "Book not available."