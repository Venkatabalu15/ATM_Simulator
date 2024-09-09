class ATM:
    def _init_(self):
        self.balance = 0.0

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return self.balance
        else:
            return "Insufficient funds. Please enter a lower amount."

# Create an instance of the ATM class
atm = ATM()

while True:
    print("ATM Simulator")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        balance = atm.check_balance()
        print("Current balance: ", balance)
    elif choice == '2':
        amount = float(input("Enter the amount to deposit: "))
        new_balance = atm.deposit(amount)
        print("Deposit successful. New balance: ", new_balance)
    elif choice == '3':
        amount = float(input("Enter the amount to withdraw: "))
        new_balance = atm.withdraw(amount)
        if isinstance(new_balance, str):
            print(new_balance)
        else:
            print("Withdrawal successful. New balance: ", new_balance)
    elif choice == '4':
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid input. Please select a number between 1 and 4.")