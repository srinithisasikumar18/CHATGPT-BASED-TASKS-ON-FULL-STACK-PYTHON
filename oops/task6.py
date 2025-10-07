class BankAccount:
    bank_name='SBI'
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance=self.balance+amount
        print(f"Amount deposited{amount}, Current balance{self.balance}")
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance=self.balance-amount
            print(f"{amount} withdrawn.New balance{self.balance}")
        else:
            print(f"Insufficient balance current balance{self.balance}")
    def display(self):
        print(f" welcome {self.name} to {BankAccount.bank_name} bank")
        print(f"Bank Balance{self.balance}")
        print("------------------------------------")
b1=BankAccount("srinithi",5000)
b2=BankAccount("kokila",8000)

b1.deposit(2000)
b2.deposit(2000)

b1.withdraw(4000)
b2.withdraw(4000)

BankAccount.bank_name="HDFC"
b1.display()
b2.display()