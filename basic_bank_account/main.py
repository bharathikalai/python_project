class BankAccount:

    def __init__(self,balance=0):
        self.balance = balance

    def deposit(self,amount):
        self.balance +=amount
        print(f"Deposited {amount}. current balance: {self.balance}")








def main():

    account = BankAccount()

    account.deposit(1000)

if __name__ == "__main__":
    main()