class BankAccount:
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def display_balance(self):
        print(f"Account Number: {self.account_number}")
        print(f"Holder Name:{self.holder_name}")
        print(f"Balance:{self.balance}")


my_account = BankAccount("12345678910", "Erick", 1000)
my_account.display_balance()
my_account.deposit(500)
my_account.display_balance()
my_account.withdraw(200)
my_account.display_balance()
my_account.withdraw(2000)
my_account.display_balance()
