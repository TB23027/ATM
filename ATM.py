attempts = 0
balance = 0.00
history = []
pin = 1234

def check_balance():
    print(f"${balance}")

def withdraw():
    print(f"Your current balance is: {balance}")
    withdraw_amount = int(input("Enter how much you would like to withdraw: "))
    new_amount = (balance - withdraw_amount)
    if new_amount <= 0:        
        print("Insufficient funds")

    else:
        print(f"Balance updated, {withdraw_amount} withdrawn")
        history.append(f"{withdraw_amount} taken out")
        balance = new_amount

def deposit():
    print(f"Your current balance is: ${balance}")
    try:
        deposited = int(input("How much would you like to deposit: "))
        new_amount = (balance + deposited)
        print(f"${deposited} added to balance")
        print(f"New amount is: {new_amount}")
        balance = new_amount
    except ValueError:
        print("Must be a valid number/integer!")



        
        


