# services/library.py - This will update to save after borrow/return
import my_data.data as data

def borrow_book(title):
    for book in data.get_books():
        if book["title"].lower() == title.lower() and book["available"]:
            book["available"] = False
            data.save_books()
            return f"You have borrowed '{book['title']}'"
    return "Book not available."

def return_book(title):
    for book in data.get_books():
        if book["title"].lower() == title.lower() and not book["available"]:
            book["available"] = True
            data.save_books()
            return f"You have returned '{book['title']}'"
    return "Book not found or not borrowed."