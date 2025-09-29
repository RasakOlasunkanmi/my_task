# Nigeria currency converter
# collcting currency
amount_in_naira = float(input("Enter the Naira amount: "))
usd_exchange_rate = float(input("Enter US Dollars exchange rate to naira: "))
gbp_exchange_rate = float(input("Enter British Pounds exchange rate to naira: "))

# Currency converter (Naira to USD & Naira to GBP)
amount_in_usd = amount_in_naira / usd_exchange_rate
amount_in_gbp = amount_in_naira / gbp_exchange_rate

# Result
print(f"Currency\tSymbols\t\tAmount\n---------------------------------------\nNaira\t\t₦\t\t{amount_in_naira:,.2f}\nUS Dollars\t$\t\t{amount_in_usd:,.2f}\nBritish Pounds\t£\t\t{amount_in_gbp:,.2f}")