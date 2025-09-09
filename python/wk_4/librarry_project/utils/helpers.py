# utils/helpers.py - This will handle helper functions

def format_book(book, index):
    status = "Available" if book["available"] else "Borrowed"
    return f"{index}. {book['title']} by {book['author']} - {status}"