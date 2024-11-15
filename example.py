balance = 1000
balance = int(balance)
siripin = "1234"
attempts = 0  
# pin validation

# Pin validation loop
while attempts < 3:
    pin = input("Enter your pin: ")
    attempts += 1
    
    if pin == siripin:
        print("""
        WELCOME SIR/MADAM
        HOW WOULD YOU LIKE ME TO HELP YOU:
            - Withdraw
            - Check balance
            - Deposit cash
            - Exit
        """)

        # Command loop for operations after pin is validated
        while True:
            command = input("Enter command please: ").lower()
            
            # Cash withdrawal
            if command == "withdraw":
                try:
                    amount = int(input("Enter amount: "))
                    if amount > balance:
                        print("Sorry sir! You do not have enough balance.")
                        print(f"Your balance is {balance}")
                    else:
                        confirmation = input(f"Are you sure you want to withdraw {amount}? (yes/no): ").lower()
                        if confirmation == "yes":
                            balance -= amount
                            print(f"{amount} successfully withdrawn.")
                            print(f"Your account balance is {balance}")
                        else:
                            print("Withdrawal cancelled.")
                
                except ValueError:
                    print("Invalid amount. Please enter a valid number.")
            
            # Check balance
            elif command == "check balance":
                print(f"Your account balance is {balance}")
            
            # Deposit cash
            elif command == "deposit cash":
                try:
                    amount = int(input("Enter amount to deposit: "))
                    balance += amount
                    print(f"Your account balance is {balance}")
                except ValueError:
                    print("Invalid amount. Please enter a valid number.")
            
            # Exit program
            elif command == "exit":
                print("Program closed.")
                break
            
            # Invalid command
            else:
                print("Sorry sir/madam, the command is invalid! Please enter a valid command.")
        
        break  # Exit after the user successfully logged in

    else:
        print(f"Sorry. Try again. You have {3 - attempts} remaining chances.")

else:
    print("Sorry ma'am! Out of chances!!")
