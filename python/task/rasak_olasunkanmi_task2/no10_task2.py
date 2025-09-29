# School fee breakdown
# collecting data
school_name = input("Enter the name: ")
tuition_fee = float(input("Enter school tuition fee: "))
hostel_fee = float(input("Enter school school fee: "))
feeding_fee = float(input("Enter feeding fee: "))

# Total fee
total = tuition_fee + hostel_fee + feeding_fee

# output
print(f"School name\t{school_name}\nTuition fee\t{tuition_fee:.2f}\nHostel fee\t{hostel_fee:.2f}\nTotal fee\t{total:.2f}")