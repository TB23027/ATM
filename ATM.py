attempts = 0
balance = 0.00
history = []
pin = 1234

def check_balance():
    print(f"${balance}")
    
def withdraw():
    global balance  
    print(f"Your current balance is: {balance}")
    try:
        withdraw_amount = int(input("Enter how much you would like to withdraw: "))
        new_amount = (balance - withdraw_amount)
        if new_amount < 0:        
            print("Insufficient funds")
        else:
            print(f"Balance updated, {withdraw_amount} withdrawn")
            history.append(f"{withdraw_amount} taken out")
            balance = new_amount
    except ValueError:
        print("Must be a valid number/integer!")

def deposit():
    global balance   
    print(f"Your current balance is: ${balance}")
    try:
        deposited = int(input("How much would you like to deposit: "))
        new_amount = (balance + deposited)
        print(f"${deposited} added to balance")
        print(f"New amount is: {new_amount}")
        balance = new_amount
        history.append(f"{deposited} deposited into atm")
    except ValueError:
        print("Must be a valid number/integer!")

def transaction_history():
    print(history)

def main():
    print("Welcome to the ATM!")
    
    
    attempts = 0
    while attempts < 3:
        try:
            user_pin = int(input("Please enter your PIN: "))
            if user_pin == pin:
                print("PIN accepted. Access granted.")
                break
            else:
                attempts += 1
                print(f"Incorrect PIN. You have {3 - attempts} attempts left.")
        except ValueError:
            print("PIN must be a number.")
            attempts += 1

    if attempts == 3:
        print("Too many failed attempts. Exiting program.")
        return
    
    
    options = {
        1: check_balance,
        2: withdraw,
        3: deposit,
        4: transaction_history,
        5: exit
    }

    while True:
        try:
            print("\nOption 1. Check balance.")
            print("Option 2. Withdraw money.")
            print("Option 3. Deposit money.")
            print("Option 4. View transaction history.")
            print("Option 5. Exit the program.")
            choice = int(input("What would you like to do? (1-5): "))

            if choice in options:
                options[choice]()
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Enter a valid number.")

if __name__ == "__main__":
    main()
