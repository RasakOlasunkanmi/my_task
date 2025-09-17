# import json
# from tabulate import tabulate


# DATA_USERS = "data/users.json"
# DATA_MARKET = "data/market_prices.json"
# DATA_HARVESTS = "data/harvests.json"


# def buyer_welcome(buyer):
#     return f"Welcome {buyer['name']}! You are logged in as a Buyer."


# def buyer_compare_prices(crop_name):
#     with open(DATA_MARKET, "r") as f:
#         prices = json.load(f)

#     if crop_name not in prices:
#         return f"No price data for {crop_name}."

#     table = [(loc, price) for loc, price in prices[crop_name].items()]
#     return tabulate(table, headers=["Location", "Price"], tablefmt="grid")


# def buyer_find_farmers_by_location(location):
#     with open(DATA_USERS, "r") as f:
#         users = json.load(f)

#     farmers = [
#         {
#             "name": u["name"],
#             "location": u.get("location", ""),
#             "farm_size": u.get("farm_size", ""),
#             "crops": u.get("crops", []),
#             "phone": u["phone"]
#         }
#         for u in users if u.get("role") == "Farmer" and u.get("location") == location
#     ]

#     if not farmers:
#         return f"No farmers found in {location}."

#     table = [
#         (f["name"], f["location"], f["farm_size"], ", ".join(f["crops"]), f["phone"])
#         for f in farmers
#     ]
#     return tabulate(table, headers=["Farmer", "Location", "Farm Size", "Crops", "Phone"], tablefmt="grid")


# def buyer_view_produce(location=None):
#     with open(DATA_HARVESTS, "r") as f:
#         harvests = json.load(f)

#     if location:
#         harvests = [h for h in harvests if h["location"] == location]

#     if not harvests:
#         return f"No produce listings{' in ' + location if location else ''}."

#     table = [
#         (h["farmer_name"], h["location"], h["crop"], h["qty"], h["price"])
#         for h in harvests
#     ]
#     return tabulate(table, headers=["Farmer", "Location", "Crop", "Qty", "Price"], tablefmt="grid")


# import json, os
# from services.market_service import compare_prices
# from services.harvest_service import search_harvests
# from services.user_service import load_json

# DATA_DIR = "data"
# USERS_FILE = os.path.join(DATA_DIR, "users.json")

# def buyer_welcome(user):
#     return f"\n🌾 Welcome {user['name']}! You are logged in as Buyer.\n"

# def buyer_compare_prices(crop_name):
#     data = compare_prices(crop_name)
#     if not data:
#         print(f"No price data available for {crop_name}.")
#         return False
    
#     # Neatly printed table
#     print(f"\n📊 Market price comparison for {crop_name}:")
#     print("-" * 40)
#     print(f"{'Location':<15}{'Price (₦)':<10}")
#     print("-" * 40)
#     for loc, price in data.items():
#         print(f"{loc:<15}{price:<10}")
#     print("-" * 40)
#     return True

# def buyer_find_farmers_by_location(location):
#     users = load_json(USERS_FILE)
#     farmers = [u for u in users if u["role"] == "Farmer" and u["location"].lower() == location.lower()]
    
#     if not farmers:
#         print(f"No farmers found in {location}.")
#         return []
    
#     print(f"\n👩‍🌾 Farmers in {location}:")
#     print("-" * 65)
#     print(f"{'Farmer ID':<12}{'Name':<15}{'Location':<12}{'Farm Size':<12}{'Primary Crops'}")
#     print("-" * 65)
#     for idx, farmer in enumerate(farmers, 1):
#         crops = ", ".join(farmer.get("crops", []))
#         print(f"{idx:<12}{farmer['name']:<15}{farmer['location']:<12}{farmer.get('farm_size','-'):<12}{crops}")
#     print("-" * 65)
#     return farmers

# def buyer_view_produce():
#     choice = input("Do you want to view produce by location? (yes/no): ").strip().lower()
    
#     location = None
#     if choice == "yes":
#         location = input("Enter location: ").strip()
    
#     results = search_harvests("", location=location) if location else search_harvests("")
    
#     if not results:
#         print("No produce found.")
#         return []
    
#     print("\n📦 Farmers' Produce Listings:")
#     print("-" * 70)
#     print(f"{'Farmer':<15}{'Location':<12}{'Crop':<12}{'Qty':<8}{'Price (₦)':<10}")
#     print("-" * 70)
#     for h in results:
#         print(f"{h['farmer_name']:<15}{h['location']:<12}{h['crop']:<12}{h['qty']:<8}{h['price']:<10}")
#     print("-" * 70)
#     return results


# # ---------------------------
# # 🟢 Buyer Menu (USSD-style)
# # ---------------------------
# def buyer_menu(user):
#     while True:
#         print("\n📱 Buyer Menu")
#         print("1. Compare market prices")
#         print("2. Find farmers by location")
#         print("3. View farmers' produce")
#         print("0. Logout")

#         choice = input("Enter choice: ").strip()

#         if choice == "1":
#             crop = input("Enter crop name to compare prices: ").strip()
#             buyer_compare_prices(crop)
#         elif choice == "2":
#             loc = input("Enter location to search farmers: ").strip()
#             buyer_find_farmers_by_location(loc)
#         elif choice == "3":
#             buyer_view_produce()
#         elif choice == "0":
#             print("Logging out... 👋")
#             break
#         else:
#             print("Invalid choice. Please try again.")




# from buyer_menu_demo import run_buyer_demo

# def main_menu():
#     """Main USSD Menu Prototype"""
#     while True:
#         print("\n=== Main Menu ===")
#         print("1. Farmer Login (placeholder)")
#         print("2. Buyer Login")
#         print("#00. Exit")

#         choice = input("Select option: ").strip()

#         if choice == "1":
#             print("👩‍🌾 Farmer login is not implemented yet (coming soon).")

#         elif choice == "2":
#             run_buyer_demo()  # calls Buyer flow
#             # When buyer exits with option 9, control returns here

#         elif choice == "#00":
#             print("✅ Exiting session. Goodbye!")
#             exit(0)

#         else:
#             print("⚠️ Invalid option. Please try again.")


# if __name__ == "__main__":
#     main_menu()



# from services.buyer_service import (
#     login_buyer, buyer_welcome, buyer_compare_prices,
#     buyer_find_farmers_by_location, buyer_view_produce
# )

# def buyer_menu(buyer):
#     """USSD-style menu for Buyers"""
#     while True:
#         print("\n=== Buyer Menu ===")
#         print("1. Compare Prices")
#         print("2. Find Farmers by Location")
#         print("3. View Produce Listings")
#         print("0. Back")
#         print("9. Main Menu")
#         print("#00. Exit")

#         choice = input("Select option: ").strip()

#         if choice == "1":
#             crop = input("Enter crop name: ").capitalize()
#             print(buyer_compare_prices(crop))

#         elif choice == "2":
#             location = input("Enter location: ").capitalize()
#             print(buyer_find_farmers_by_location(location))

#         elif choice == "3":
#             sub = input("Do you want to filter by location? (yes/no): ").lower()
#             if sub == "yes":
#                 location = input("Enter location: ").capitalize()
#                 print(buyer_view_produce(location))
#             else:
#                 print(buyer_view_produce())

#         elif choice == "0":
#             print("⬅️ Going back...")
#             continue  # here just refreshes menu (in full system it goes back one level)

#         elif choice == "9":
#             print("🏠 Returning to Main Menu (placeholder)...")
#             break  # later will link to real MainMenu

#         elif choice == "#00":
#             print("✅ Exiting session. Goodbye!")
#             exit(0)

#         else:
#             print("⚠️ Invalid option. Please try again.")


# def run_buyer_demo():
#     print("=== Buyer Login ===")
#     phone = input("Enter your phone number: ")
#     pin = input("Enter your PIN: ")

#     buyer = login_buyer(phone, pin)

#     if not buyer:
#         print("❌ Login failed. Invalid credentials or not a Buyer.")
#         return

# #     print(buyer_welcome(buyer))
# #     buyer_menu(buyer)


# # if __name__ == "__main__":
# #     run_buyer_demo()



# from tabulate import tabulate

# # --- Mock Data (standalone mode, no JSON files needed) ---
# USERS = [
#     {
#         "name": "Aliu",
#         "phone": "08033334444",
#         "pin": "5678",
#         "role": "Buyer",
#         "location": "Lagos"
#     },
#     {
#         "name": "Chinedu",
#         "phone": "08022221111",
#         "pin": "1234",
#         "role": "Farmer",
#         "location": "Lagos",
#         "farm_size": "5 acres",
#         "crops": ["Maize", "Cassava"]
#     }
# ]

# MARKET_PRICES = {
#     "Maize": {"Lagos": 150, "Kano": 120, "Abuja": 140},
#     "Cassava": {"Lagos": 90, "Ibadan": 80}
# }

# HARVESTS = [
#     {"farmer_name": "Chinedu", "location": "Lagos", "crop": "Maize", "qty": 200, "price": 150},
#     {"farmer_name": "Chinedu", "location": "Lagos", "crop": "Cassava", "qty": 500, "price": 90}
# ]

# # --- Buyer Features ---
# def login_buyer(phone, pin):
#     """Simple login with error handling"""
#     try:
#         buyer = next(u for u in USERS if u["phone"] == phone and u["pin"] == pin and u["role"] == "Buyer")
#         return buyer
#     except StopIteration:
#         return None


# def buyer_welcome(buyer):
#     try:
#         return f"Welcome {buyer['name']}! You are logged in as a Buyer."
#     except Exception:
#         return "Error: Invalid buyer profile."


# def buyer_compare_prices(crop_name):
#     try:
#         if crop_name not in MARKET_PRICES:
#             return f"⚠️ No price data available for {crop_name}."

#         table = [(loc, price) for loc, price in MARKET_PRICES[crop_name].items()]
#         return tabulate(table, headers=["Location", "Price"], tablefmt="grid")
#     except Exception as e:
#         return f"Error comparing prices: {e}"


# def buyer_find_farmers_by_location(location):
#     try:
#         farmers = [
#             {
#                 "name": u["name"],
#                 "location": u.get("location", ""),
#                 "farm_size": u.get("farm_size", ""),
#                 "crops": u.get("crops", []),
#                 "phone": u["phone"]
#             }
#             for u in USERS if u.get("role") == "Farmer" and u.get("location") == location
#         ]

#         if not farmers:
#             return f"⚠️ No farmers found in {location}."

#         table = [
#             (f["name"], f["location"], f["farm_size"], ", ".join(f["crops"]), f["phone"])
#             for f in farmers
#         ]
#         return tabulate(table, headers=["Farmer", "Location", "Farm Size", "Crops", "Phone"], tablefmt="grid")
#     except Exception as e:
#         return f"Error finding farmers: {e}"


# def buyer_view_produce(location=None):
#     try:
#         harvests = HARVESTS
#         if location:
#             harvests = [h for h in harvests if h["location"] == location]

#         if not harvests:
#             return f"⚠️ No produce listings{' in ' + location if location else ''}."

#         table = [
#             (h["farmer_name"], h["location"], h["crop"], h["qty"], h["price"])
#             for h in harvests
#         ]
#         return tabulate(table, headers=["Farmer", "Location", "Crop", "Qty", "Price"], tablefmt="grid")
#     except Exception as e:
#         return f"Error viewing produce: {e}"





from tabulate import tabulate


USERS = [
    {
        "name": "Aliu",
        "phone": "08033334444",
        "pin": "5678",
        "role": "Buyer",
        "location": "Lagos"
    },
    {
        "name": "Chinedu",
        "phone": "08022221111",
        "pin": "1234",
        "role": "Farmer",
        "location": "Lagos",
        "farm_size": "5 acres",
        "crops": ["Maize", "Cassava"]
    }
]

MARKET_PRICES = {
    "Maize": {"Lagos": 150, "Kano": 120, "Abuja": 140},
    "Cassava": {"Lagos": 90, "Ibadan": 80}
}

HARVESTS = [
    {"farmer_name": "Chinedu", "location": "Lagos", "crop": "Maize", "qty": 200, "price": 150},
    {"farmer_name": "Chinedu", "location": "Lagos", "crop": "Cassava", "qty": 500, "price": 90}
]


# --- Buyer Features ---
def login_buyer(phone, pin):
    """Simple login with error handling"""
    try:
        return next(
            u for u in USERS
            if u["phone"] == phone and u["pin"] == pin and u["role"] == "Buyer"
        )
    except StopIteration:
        return None


def buyer_welcome(buyer):
    try:
        return f"Welcome {buyer['name']}! You are logged in as a Buyer."
    except Exception:
        return "Error: Invalid buyer profile."


def buyer_compare_prices(crop_name):
    try:
        if crop_name not in MARKET_PRICES:
            return f"No price data available for {crop_name}."

        table = [(loc, price) for loc, price in MARKET_PRICES[crop_name].items()]
        return tabulate(table, headers=["Location", "Price"], tablefmt="grid")
    except Exception as e:
        return f"Error comparing prices: {e}"


def buyer_find_farmers_by_location(location):
    try:
        farmers = [
            {
                "name": u["name"],
                "location": u.get("location", ""),
                "farm_size": u.get("farm_size", ""),
                "crops": u.get("crops", []),
                "phone": u["phone"]
            }
            for u in USERS if u.get("role") == "Farmer" and u.get("location") == location
        ]

        if not farmers:
            return f"No farmers found in {location}."

        table = [
            (f["name"], f["location"], f["farm_size"], ", ".join(f["crops"]), f["phone"])
            for f in farmers
        ]
        return tabulate(
            table,
            headers=["Farmer", "Location", "Farm Size", "Crops", "Phone"],
            tablefmt="grid"
        )
    except Exception as e:
        return f"Error finding farmers: {e}"


def buyer_view_produce(location=None):
    try:
        harvests = HARVESTS
        if location:
            harvests = [h for h in harvests if h["location"] == location]

        if not harvests:
            return f"No produce listings{' in ' + location if location else ''}."

        table = [
            (h["farmer_name"], h["location"], h["crop"], h["qty"], h["price"])
            for h in harvests
        ]
        return tabulate(
            table,
            headers=["Farmer", "Location", "Crop", "Qty", "Price"],
            tablefmt="grid"
        )
    except Exception as e:
        return f"Error viewing produce: {e}"


# --- Buyer USSD Menu ---
def run_buyer_demo():
    phone = input("Enter your phone number: ").strip()
    pin = input("Enter your PIN: ").strip()
    buyer = login_buyer(phone, pin)

    if not buyer:
        print("Login failed. Invalid phone or PIN.")
        return

    # Show welcome note
    print(buyer_welcome(buyer))

    # Menu loop
    while True:
        print("\n=== Buyer Menu ===")
        print("1. Compare Prices")
        print("2. Find Farmers by Location")
        print("3. View Produce Listings")
        print("0. Back")
        print("9. Main Menu")
        print("#00. Exit")

        choice = input("Select option: ").strip()

        if choice == "1":
            crop = input("Enter crop name: ").capitalize()
            print(buyer_compare_prices(crop))

        elif choice == "2":
            location = input("Enter location: ").capitalize()
            print(buyer_find_farmers_by_location(location))

        elif choice == "3":
            yn = input("Do you want to filter by location? (yes/no): ").strip().lower()
            if yn == "yes":
                loc = input("Enter location: ").capitalize()
                print(buyer_view_produce(loc))
            else:
                print(buyer_view_produce())

        elif choice == "0":
            print("Going back (placeholder).")
            break

        elif choice == "9":
            print("Returning to Main Menu (placeholder).")
            break

        elif choice == "#00":
            print("Exiting session. Goodbye!")
            exit(0)

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    run_buyer_demo()