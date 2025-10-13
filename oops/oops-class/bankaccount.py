class BankAccount:
    amount=0
    def __init__(self,account_number, account_holder, balance):
        self.account_number=account_number
        self.account_holder=account_holder
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        return amount
    def withdraw(self,amount):
        self.balance-=amount
        return amount
    def dispaly(self):
        print(f"{b1.account_number,b1.account_holder}'s balance is {self.balance}")
b1=BankAccount(101,"srinithi",1000)
b1.deposit(1000)
b1.withdraw(500)
b1.dispaly()
print(f"{b1.account_number,b1.account_holder}'s balance is {b1.balance}")




