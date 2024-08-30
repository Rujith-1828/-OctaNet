import getpass
from datetime import datetime

class ATM:
    def __init__(self):
        self.accounts = {}
        self.transaction_history = {}
        self.current_account = None
    
    def create_account(self, account_number, password):
        if account_number in self.accounts:
            print("Account already exists.")
        else:
            self.accounts[account_number] = {
                'password': password,
                'balance': 0
            }
            self.transaction_history[account_number] = []
            print("Account created successfully.")
    
    def login(self, account_number, password):
        if account_number in self.accounts and self.accounts[account_number]['password'] == password:
            self.current_account = account_number
            print("Login successful.")
        else:
            print("Invalid account number or password.")
    
    def check_balance(self):
        if self.current_account:
            balance = self.accounts[self.current_account]['balance']
            print(f"Your current balance is: ${balance:.2f}")
        else:
            print("Please login to check balance.")
    
    def deposit(self, amount):
        if self.current_account:
            if amount > 0:
                self.accounts[self.current_account]['balance'] += amount
                self.record_transaction("Deposit", amount)
                print(f"Deposited ${amount:.2f}.")
            else:
                print("Invalid amount. Please enter a positive number.")
        else:
            print("Please login to deposit money.")
    
    def withdraw(self, amount):
        if self.current_account:
            if amount > 0:
                if amount <= self.accounts[self.current_account]['balance']:
                    self.accounts[self.current_account]['balance'] -= amount
                    self.record_transaction("Withdraw", amount)
                    print(f"Withdrew ${amount:.2f}.")
                else:
                    print("Insufficient funds.")
            else:
                print("Invalid amount. Please enter a positive number.")
        else:
            print("Please login to withdraw money.")
    
    def change_password(self, old_password, new_password):
        if self.current_account:
            if self.accounts[self.current_account]['password'] == old_password:
                self.accounts[self.current_account]['password'] = new_password
                print("Password changed successfully.")
            else:
                print("Old password is incorrect.")
        else:
            print("Please login to change password.")
    
    def record_transaction(self, transaction_type, amount):
        if self.current_account:
            transaction = {
                'type': transaction_type,
                'amount': amount,
                'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            self.transaction_history[self.current_account].append(transaction)
    
    def view_transaction_history(self):
        if self.current_account:
            history = self.transaction_history[self.current_account]
            if history:
                print("Transaction History:")
                for txn in history:
                    print(f"{txn['date']} - {txn['type']}: ${txn['amount']:.2f}")
            else:
                print("No transaction history available.")
        else:
            print("Please login to view transaction history.")
    
    def logout(self):
        if self.current_account:
            self.current_account = None
            print("Logged out successfully.")
        else:
            print("No user is logged in.")
    
    def run(self):
        while True:
            print("\nATM Menu:")
            print("1. Create Account")
            print("2. Login")
            print("3. Check Balance")
            print("4. Deposit")
            print("5. Withdraw")
            print("6. Change Password")
            print("7. View Transaction History")
            print("8. Logout")
            print("9. Exit")
            choice = input("Select an option: ")
            
            if choice == '1':
                acc_number = input("Enter account number: ")
                password = getpass.getpass("Enter password: ")
                self.create_account(acc_number, password)
            elif choice == '2':
                acc_number = input("Enter account number: ")
                password = getpass.getpass("Enter password: ")
                self.login(acc_number, password)
            elif choice == '3':
                self.check_balance()
            elif choice == '4':
                try:
                    amount = float(input("Enter amount to deposit: "))
                    self.deposit(amount)
                except ValueError:
                    print("Invalid amount. Please enter a numeric value.")
            elif choice == '5':
                try:
                    amount = float(input("Enter amount to withdraw: "))
                    self.withdraw(amount)
                except ValueError:
                    print("Invalid amount. Please enter a numeric value.")
            elif choice == '6':
                old_password = getpass.getpass("Enter old password: ")
                new_password = getpass.getpass("Enter new password: ")
                self.change_password(old_password, new_password)
            elif choice == '7':
                self.view_transaction_history()
            elif choice == '8':
                self.logout()
            elif choice == '9':
                print("Exiting...")
                break
            else:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    atm = ATM()
    atm.run()
