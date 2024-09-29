#bank account
#deposit
#withdraw
#check balance
#customer details

class BankAccount:
    def __init__(self,account_number,date_of_opening,balance,customer_name):

        self.account_number=account_number
        self.date_of_opening=date_of_opening
        self.balance=balance
        self.customer_name=customer_name

        
    def deposit(self,amount):
        self.balance +=amount
        print(f"{amount} deposited successfully")

    def withdraw(self,amount):
        if self.balance <amount:
            print("insuficient balance")
        else:
            self.balance -=amount
            print(f"{amount} withdrawed successfully")
            
        
    def check_balance(self):
        print(f"your balance amount: {self.balance}")

    def show_details(self):
        print(f"account_number: {self.account_number}")
        print(f"name: {self.customer_name}")
        print(f"balance: {self.balance}")
        print(f"date_of_opening: {self.date_of_opening}")
        
acct_01=BankAccount("420132478","12/2/2024",24000,"Anju")#object creation
acct_01.deposit(1000)
acct_01.check_balance()
acct_01.withdraw(450)
acct_01.check_balance()

acct_01.show_details()








    #s=int(input("enter your balance"))
    #acct_01=BankAccount("420132478","12/2/2024",24000,"Anju")


acct_02=BankAccount(34652788,18/9/2023,30000,"sree")



