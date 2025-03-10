# Global variables to store ATM state
attempts = 0  # Tracks the number of incorrect PIN attempts
balance = 0.00  # Stores the user's account balance
history = []  # Stores the transaction history
pin = 1234  # Predefined PIN for accessing the ATM services

# Function to check the account balance
def check_balance():
    # Displays the current balance to the user
    print(f"${balance}")

# Function to withdraw money from the account
def withdraw():
    # Enables modification of the global balance variable
    global balance  
    print(f"Your current balance is: {balance}")
    try:
        # Prompt the user to input a withdrawal amount
        withdraw_amount = int(input(
            "Enter how much you would like to withdraw: "
        ))
        # Calculate the new balance
        new_amount = balance - withdraw_amount  

        # Check if funds are insufficient and inform the user
        if new_amount < 0:
            print("Insufficient funds")
        else:
            # Update balance and record the successful transaction
            print(f"Balance updated, ${withdraw_amount} withdrawn")
            history.append(f"${withdraw_amount} withdrawn")
            balance = new_amount  # Update the global balance
    except ValueError:
        # Handles invalid input when a non-integer is entered
        print("Must be a valid number/integer!")

# Function to deposit money into the account
def deposit():
    # Enables modification of the global balance variable
    global balance  
    print(f"Your current balance is: ${balance}")
    try:
        # Prompt the user to input a deposit amount
        deposited = int(input(
            "How much would you like to deposit: "
        ))
        new_amount = balance + deposited  # Calculate the new balance

        # Update balance and inform the user about the transaction
        print(f"${deposited} added to balance")
        print(f"New amount is: ${new_amount}")
        balance = new_amount  # Update the global balance
        # Record the successful transaction in the history list
        history.append(f"${deposited} deposited")
    except ValueError:
        # Handles invalid input when a non-integer is entered
        print("Must be a valid number/integer!")

# Function to display the transaction history
def transaction_history():
    # Print all recorded transactions for the user
    print(history)

# Main function to handle the ATM operations
def main():
    # Display a welcome message to the user
    print("Welcome to the ATM!")

    # PIN verification process
    attempts = 0  # Local variable to track incorrect attempts
    while attempts < 3:
        try:
            # Prompt the user to input their PIN
            user_pin = int(input("Please enter your PIN: "))
            if user_pin == pin:  # Validate the entered PIN
                print("PIN accepted. Access granted.")
                break  # Exit the loop when the correct PIN is entered.
            else:
                attempts += 1  # Increment the attempts counter
                print(f"Incorrect PIN. You have {3 - attempts} attempts left.")
        except ValueError:
            # Handles invalid input when a non-integer is entered.
            print("PIN must be a number.")
            attempts += 1

    # Exit the program if the user fails to input the correct PIN.
    if attempts == 3:
        print("Too many failed attempts. Exiting program.")
        return

    # Dictionary to map user menu choices to their respective functions
    options = {
        1: check_balance,  # Check account balance
        2: withdraw,  # Withdraw money
        3: deposit,  # Deposit money
        4: transaction_history,  # View transaction history
        5: exit  # Exit the program
    }

    # Main loop to present user menu and execute selected options
    while True:
        try:
            # Display ATM menu options
            print("\nOption 1. Check balance.")
            print("Option 2. Withdraw money.")
            print("Option 3. Deposit money.")
            print("Option 4. View transaction history.")
            print("Option 5. Exit the program.")

            # Prompt the user to select an option
            choice = int(input("What would you like to do? (1-5): "))

            if choice in options:  # Validate the user's choice
                options[choice]()  # Call the corresponding function
            else:
                # Inform the user if the choice is invalid
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            # Handles invalid input when a non-integer is entered.
            print("Enter a valid number.")

# Entry point of the program
if __name__ == "__main__":
    main()
