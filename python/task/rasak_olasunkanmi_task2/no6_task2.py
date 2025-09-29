# Electricity Bill Formatter
# collecting data
full_name = input("Enter your full name: ") # customer name
unit_consumed = int(input("Enter the unit consumed (KWh): "))
cost_per_unit = float(input("Enter the cost per unit: "))

# Total bills
total_bill = unit_consumed * cost_per_unit

# receipt of the electricity bills
print(f"Service\t\t\tUnit Consume\tCost per unit\tTotal bills\n--------------------------------------------------------------------\nElectricity consume\t{unit_consumed:,}\t\t{cost_per_unit:,}\t\t{total_bill:,}")