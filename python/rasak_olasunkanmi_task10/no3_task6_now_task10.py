# Task3: Simulate a football match ticket system
# - Store all seat numbers (1 to 50) in a set.
# - Ask users to "book" a seat by entering the number.
# - Remove booked seats from the set.
# - Show remaining seats after each booking.

seat_numbers = {x: x for x in range(1, 51)}

try:
    for _ in range(3):  # allow 3 bookings (you can change this number)
        try:
            book = int(input("Enter the seat number you want to book (1-50): "))
            booked_seat = seat_numbers.pop(book, None)
            if booked_seat:
                print(f"Booked seat: {booked_seat}")
            else:
                print("Seat already booked or invalid number.")
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 50.")
finally:
    print("\nRemaining seats:", sorted(seat_numbers.values()))