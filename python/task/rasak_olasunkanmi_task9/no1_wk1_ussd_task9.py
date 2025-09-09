
# USSD Simulation with Loop (no error handling)

while True:
    print("\nWelcome to MyBank USSD Service")
    print("1. Airtime Purchase")
    print("2. Data Purchase")
    print("3. Check Balance")
    print("Type 'exit' to quit")

    # Step 1: Choose service
    service = input("Enter the number of your choice: ")
    if service.lower() == "exit":
        print("Exiting USSD service...")
        break

    # Step 2: Network selection for Airtime or Data
    network = input("Enter your network: ")

    # Step 3: Amount entry for Airtime or Data
    amount = float(input("Enter amount: "))

    # Step 4: Confirmation menu
    print("1. Send")
    print("2. Cancel")
    action = input("Enter your choice: ")

    # Step 5: Display transaction summary
    print("\n--- USSD Transaction Summary ---")
    if service == "1":
        print("Service: Airtime Purchase")
    elif service == "2":
        print("Service: Data Purchase")
    else:
        print("Service: Balance Check")

    print("Network:", network)
    print("Amount:", amount)
    print("Action:", action)
    print("Transaction Complete!" if action == "1" else "Transaction Cancelled")