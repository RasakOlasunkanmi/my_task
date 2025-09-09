"""
We’ll treat this in two layers:

Prototype (Step 1: due tomorrow) → A single Python file (prototype.py) with everything working (registration, login, USSD menus, file persistence). This is the "proof-of-concept" version.

Final structured project (Step 2–4) → Each group member works on their assigned part inside the folder structure, pushes to GitHub individually, then merges later.
"""


"""This is the prototype.py. It covers:
- Farmer/Buyer registration/login (with PIN).
- Harvest recording (Farmer).
- Product search (Buyer).
- Market prices (JSON-based).
- USSD-like menus with 0, 9, #00.
"""


""" Step 2: Split Tasks (Final Structure)

Now, when moving to the full project, here’s what each person codes inside the folder:

>>> Person A — Models (src/models/)

user.py (User ABC)

farmer.py (Farmer)

buyer.py (Buyer)

product.py (Product ABC)

crop.py (Crop)

harvest.py (Harvest class)

>>> Person B — Services (src/services/)

user_service.py (register, login, update)

market_service.py (prices, trends)

harvest_service.py (record, inventory)

connection_service.py (buyer ↔ farmer directory)

>>> Person C — Interfaces (src/interfaces/)

base_interface.py (USSDInterface ABC)

main_menu.py

farmer_menu.py

buyer_menu.py

session_manager.py

>>> Person D — Utilities + Integration (src/utils/ + main.py)

data_handler.py (load/save JSON)

validators.py (PIN, phone, etc.)

helpers.py (formatting, menu)

main.py (ties everything together
"""



"""Step 1: Prototype (what to submit first)

The first milestone doesn’t require the full folder structure, tests, or docs — just a single working USSD CLI app that proves the concept.

Must-have prototype features:

Registration/Login with PIN (Farmer/Buyer)

Check market prices (real-time from market_prices.json)

Farmer: record harvests, create listings

Buyer: search for products, get farmer contact

USSD menus with back (0), main (9), exit (#00)

File-based persistence (users.json, harvests.json, market_prices.json, connections.json)

Basic OOP:

Abstract classes for User, Product, USSDInterface

Inherit Farmer/Buyer, Crop etc
"""


"""Prototype Overview

This is a USSD-style CLI app that simulates how farmers and buyers can interact with a digital market.

What it can do:

Register/Login with phone + PIN (as Farmer or Buyer).

Farmer can record harvests & create product listings.

Buyer can search for products & get farmer contacts.

Check market prices (from market_prices.json).

Navigation:

0 → Back

9 → Main Menu

#00 → Exit

Tech rules:

Persistence: data stored in JSON files (users.json, harvests.json, etc.).

OOP:

Abstract classes (User, Product, USSDInterface).

Subclasses (Farmer, Buyer, Crop).

Harvest model.

Single-file prototype (no big folder structure yet).
"""


"""
1. Models (Person A)

Defines who uses the system (Farmer, Buyer) and what they produce (Harvest, Crop).
2. Services (Person B)

Handle business logic → register, login, record harvest, search products, check market prices.
3. USSD Interface (Person C)

Simulates menus & navigation.
4. Run the Prototype
"""

"""In Summary...

We used OOP → abstract base classes, inheritance for Farmer/Buyer, Harvest model.

We used JSON persistence → users.json, harvests.json, market_prices.json.

We simulated USSD navigation → menus with back (0), main (9), exit (#00).

Farmers → record harvests, check prices.

Buyers → search crops, see farmer contacts.

Market prices come from a JSON file instead of real API (but extensible later).
"""


"""Demo Run (Example)

=== AgroUSSD Main Menu ===
1. Register
2. Login
#00. Exit
Select option: 1

Name: Adamu
Phone: 08011112222
Location: Kano
PIN: 1234
Register as (F=Farmer, B=Buyer): F
Farm size: 2 hectares
Farmer registered successfully!

=== AgroUSSD Main Menu ===
1. Register
2. Login
#00. Exit
Select option: 2
Phone: 08011112222
PIN: 1234
Welcome Adamu (Farmer)

--- Farmer Menu ---
1. Record Harvest
2. Check Market Prices
0. Back
Select option: 1
Crop: Tomato
Quantity: 500
Price: 1500
Harvest recorded!
"""

[
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


{
  "Maize": {"Lagos": 150, "Kano": 120, "Abuja": 140},
  "Cassava": {"Lagos": 90, "Ibadan": 80}
}


[
  {
    "farmer_name": "Chinedu",
    "location": "Lagos",
    "crop": "Maize",
    "qty": 200,
    "price": 150
  },
  {
    "farmer_name": "Chinedu",
    "location": "Lagos",
    "crop": "Cassava",
    "qty": 500,
    "price": 90
  }
]


# ---------------------------
# 🟢 Buyer Menu (USSD-style)
# ---------------------------
def buyer_menu(user):
    while True:
        print("\n📱 Buyer Menu")
        print("1. Compare market prices")
        print("2. Find farmers by location")
        print("3. View farmers' produce")
        print("0. Logout")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            crop = input("Enter crop name to compare prices: ").strip()
            buyer_compare_prices(crop)
        elif choice == "2":
            loc = input("Enter location to search farmers: ").strip()
            buyer_find_farmers_by_location(loc)
        elif choice == "3":
            buyer_view_produce()
        elif choice == "0":
            print("Logging out... 👋")
            break
        else:
            print("Invalid choice. Please try again.")





from services.user_service import login_user
from services.buyer_service import (
    buyer_welcome, buyer_compare_prices,
    buyer_find_farmers_by_location, buyer_view_produce
)

# Login as a buyer (assuming already registered)
buyer = login_user("08033334444", "5678")
if buyer and buyer["role"] == "Buyer":
    print(buyer_welcome(buyer))

    # 1) Compare prices
    buyer_compare_prices("Tomato")

    # 2) Find farmers in Kano
    buyer_find_farmers_by_location("Kano")

    # 3) View produce (location filter optional)
    buyer_view_produce()
else:
    print("Buyer login failed or user is not a Buyer.")








import json, os
from services.market_service import compare_prices
from services.harvest_service import search_harvests
from services.user_service import load_json

DATA_DIR = "data"
USERS_FILE = os.path.join(DATA_DIR, "users.json")

def buyer_welcome(user):
    return f"\n🌾 Welcome {user['name']}! You are logged in as Buyer.\n"

def buyer_compare_prices(crop_name):
    data = compare_prices(crop_name)
    if not data:
        return f"No price data available for {crop_name}."
    
    # Neatly printed table
    print(f"\nMarket price comparison for {crop_name}:")
    print("-" * 40)
    print(f"{'Location':<15}{'Price (₦)':<10}")
    print("-" * 40)
    for loc, price in data.items():
        print(f"{loc:<15}{price:<10}")
    print("-" * 40)
    return True

def buyer_find_farmers_by_location(location):
    users = load_json(USERS_FILE)
    farmers = [u for u in users if u["role"] == "Farmer" and u["location"].lower() == location.lower()]
    
    if not farmers:
        print(f"No farmers found in {location}.")
        return []
    
    print(f"\n👩‍🌾 Farmers in {location}:")
    print("-" * 60)
    print(f"{'Farmer ID':<12}{'Name':<15}{'Location':<12}{'Farm Size':<12}{'Primary Crops'}")
    print("-" * 60)
    for idx, farmer in enumerate(farmers, 1):
        crops = ", ".join(farmer.get("crops", []))
        print(f"{idx:<12}{farmer['name']:<15}{farmer['location']:<12}{farmer.get('farm_size','-'):<12}{crops}")
    print("-" * 60)
    return farmers

def buyer_view_produce():
    choice = input("Do you want to view produce by location? (yes/no): ").strip().lower()
    
    location = None
    if choice == "yes":
        location = input("Enter location: ").strip()
    
    results = search_harvests("", location=location) if location else search_harvests("")
    
    if not results:
        print("No produce found.")
        return []
    
    print("\n📦 Farmers' Produce Listings:")
    print("-" * 70)
    print(f"{'Farmer':<15}{'Location':<12}{'Crop':<12}{'Qty':<8}{'Price (₦)':<10}")
    print("-" * 70)
    for h in results:
        print(f"{h['farmer_name']:<15}{h['location']:<12}{h['crop']:<12}{h['qty']:<8}{h['price']:<10}")
    print("-" * 70)
    return results
