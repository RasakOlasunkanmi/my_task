# Task2: Super Market Price List
# - Create a program that stores items and their prices in a dictionary.
#   - Items should come from a list.
#   - Prices are entered by the user.
#   - Display all items and prices, then allow the user to update the price of an item.
# - Requirements:
#   - Use dictionary update method `.update()` or assignment.
#   - Use `.keys()` to display available items.
#   - Use input validation (no advanced functions).

super_market_prices = {}
items = ["Bread", "Butter", "Sugar", "Milk", "Milo"]

try:
    super_market_prices["Bread"] = input("Enter the price of Bread: ")
    super_market_prices["Butter"] = input("Enter the price of Butter: ")
    super_market_prices["Sugar"] = input("Enter the price of Sugar: ")
    super_market_prices["Milk"] = input("Enter the price of Milk: ")
    super_market_prices["Milo"] = input("Enter the price of Milo: ")

    # Print all prices
    print(f"Bread: {super_market_prices['Bread']}")
    print(f"Butter: {super_market_prices['Butter']}")
    print(f"Sugar: {super_market_prices['Sugar']}")
    print(f"Milk: {super_market_prices['Milk']}")
    print(f"Milo: {super_market_prices['Milo']}")
    print("\nAvailable items:", list(super_market_prices.keys()))
    item_to_update = input("Enter the name of the item you want to update the price for: ")
    new_price = input(f"Enter the new price for {item_to_update}: ")

    # Try updating
    if item_to_update in super_market_prices:
        super_market_prices[item_to_update] = new_price
    else:
        raise KeyError("Invalid item entered.")

    # Print updated prices
    print("\nUpdated price list:")
    print(f"Bread: {super_market_prices['Bread']}")
    print(f"Butter: {super_market_prices['Butter']}")
    print(f"Sugar: {super_market_prices['Sugar']}")
    print(f"Milk: {super_market_prices['Milk']}")
    print(f"Milo: {super_market_prices['Milo']}")

except KeyError as e:
    print("Error:", e)

except Exception as e:
    print("An unexpected error occurred:", e)

finally:
    print("\nThank you for using SuperMarket Price Updater!")