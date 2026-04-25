import datetime
class Bank:
    def __init__(self, name, password, email, balance=0):
        self.name = name
        self.__password = password   
        self.email = email
        self.balance = balance
        print(f"Dear {self.name}, your account was created successfully!")
        history=[]

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposit successful!")
            self.history.append("Deposit            ",amount,"           ",datetime.datetime.now())
        else:
            print("Invalid amount!")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount!")
        elif amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print("Withdraw successful!")
            self.history.append("Withdrawn            ",amount,"           ",datetime.datetime.now())
    def see_profile(self):
        print("Name:", self.name)
        print("Email:", self.email)
        print("Balance:", self.balance)
        print("Password: ********")
        print("Balance: *******")
        print
    def login(self,name,password):
        if self.name==name and self.password==password:
            return True
        else:
            print("Invalid Password!Try Again...")
    def change_password(self,new_password):
        self.__password=new_password
    def show_history(self):
        print("Activity               Amount               Date and Time")


print("================================")
print("||             BANK            ||")
print("================================")
going=True
while going:
    print("1.Create New Account")
    print("2.Login")
    print("3.Exit")
    choice=int(input("What you want to do? Enter the respective number..."))
    if choice==1:
        name=input("Enter your name...:")
        password=input("Enter the password for your account...")
        email=input("Enter your email address...:")
        account1=Bank(name,password,email)
        continue
    elif choice==2:
        username=input("Enter your name..:")
        user_pass=input("Enter your password..:")
        logged_in=account1.login(username,user_pass)
        if logged_in:
            print("===============================")
            print("||____________________________||")
            while logged_in:
                print("1. See Profile Details")
                print("2.Deposit Money")
                print("3.Withdraw Money")
                print("4.Show Transactions History")
                print("5.Change Password")
                print("6.Change Password")
                print("7.Exit")
                inner_choice=int(input("Enter your choice number based on services..."))