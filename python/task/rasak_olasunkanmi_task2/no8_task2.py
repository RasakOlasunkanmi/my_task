# Transport fare calculators
distance = float(input("Enter the distance covered in \"km\": "))
fare_per_km = float(input("Enter fare price per km: "))

# Total fare
total_fare = distance * fare_per_km

# output
print(f"Total fare: {total_fare:.2f}")