# Task3: Simulate a football match ticket system
# - Store all seat numbers (1 to 50) in a set.
# - Ask users to "book" a seat by entering the number.
# - Remove booked seats from the set.
# - Show remaining seats after each booking.

seat_numbers = {x: x for x in range(1, 51)}
book = int(input("Enter the seat number you want to book (1, 50): "))
booked_seat = seat_numbers.pop(book, None)
print(f"Booked seat: {booked_seat}" if booked_seat else "Seat already booked or invalid number.")
print("Remaining seats:", sorted(seat_numbers.values()))