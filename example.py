command = ""
balance = 1000
balance = int(balance)
siripin = "1234"
withdraw = ""
x_attempt = 3
attemps = 0
x_attempt = int(x_attempt)

while attemps < x_attempt:
        pin = input("enter pin: ")
        if pin == siripin:
    
            print("""
            WELCOMES SIR/MADAM
        HOW WOULD LIKE ME TO HELP YOU:
                    Withdraw
                    check balance
                    deposit cash
                    exit
            
                """)            
            while True:
                command = input("enter command please:")
                if command == "withdraw":
                    amount = input("enter amount: ")
                    amount = int(amount)
                    if amount > balance:
                        print("Sorry sir! more than you gat")
                        print(f"Your balance is {balance}")
                    else:

                            balance = balance - amount
                            confirmation = input("Are you sure you wanna do this: ").lower()
                            if confirmation == "yes":
                                print(f"{amount} successful withdrawn.")
                            else:
                                print("Sorry but you must go.!!!")
                                exit()
                            
                elif command == "check balance":
                    print(f"Your account balance is {balance}")
                elif command == "deposit cash":
                    amount = int(input("enter amount: "))
                    balance = amount + balance
                    print(f"account balance is {balance}")
                elif command == "exit":
                    print("program closed")
                    break
                else:
                    print("sorry sir/madam: command is in valid! enter, help.")
        else:
            print("sorry. access dinayed")
            

else:
    attemps += 1
    if attemps < x_attempt:
        pin = input(f"renter pin.{x_attempt - attemps} attemps left")
    else:
        print("You sorry ass there is no room for !!!FORGOT PIN!!!")
        