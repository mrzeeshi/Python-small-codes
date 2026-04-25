import datetime
class Bank:
    def __init__(self, name, password, email, balance=0):
        self.name = name
        self.__password = password   
        self.email = email
        self.balance = balance
        print(f"Dear {self.name}, your account was created successfully!")
        self.history=[]

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposit successful!")
            self.history.append(f"Deposit            {amount}           {datetime.datetime.now()}")
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
            self.history.append(f"Withdrawn            {amount}           {datetime.datetime.now()}")
    def see_profile(self):
        print("=====Profile Details============")
        print("Name:      ", self.name)
        print("Email:      ", self.email)
        print("Balance:    ", self.balance)
        print("Password: ********")
        print("Balance: *******")
        print("=================================")
    def login(self,name,password):
        if self.name==name and self.__password==password:
            return True
        else:
            print("Invalid Password!Try Again...")
    def change_password(self,new_password):
        self.__password=new_password
    def show_history(self):
        print("Activity               Amount               Date and Time")
        for record in self.history:
            print(record)


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
                print("6.Exit")
                inner_choice=int(input("Enter your choice number based on services..."))
                if inner_choice==1:
                    account1.see_profile()
                    continue
                elif inner_choice==2:
                    deposit=int(input("Enter the amount of money you want to deposit...:"))
                    account1.deposit(deposit)
                    continue
                elif inner_choice==3:
                    withdraw=int(input("Enter the amount you want to withdraw...:"))
                    account1.withdraw(withdraw)
                    continue
                elif inner_choice==4:
                    account1.show_history()
                    continue
                elif inner_choice==5:
                    changing_pass=True
                    while changing_pass:
                        new_pass=input("Enter the new password...")
                        confirm_pass=input("Confirm new password...")
                        if new_pass==confirm_pass:
                            if len(new_pass)>=8:
                                account1.change_password(new_pass)
                                print("Password changed successfully!!!")
                                changing_pass=False
                            else:
                                print("The password must be more than or equal to 8 characters long...")
                                continue
                        else:
                            print("The both passwords are different enter them again...")
                            continue
                    continue
                elif inner_choice==6:
                    logged_in=False
                else:
                    print("Invalid Choice! Enter a valid choice.....")
                    continue
    elif choice==3:
        going=False
    else:
        print("Enter the valid choice between 1 and 3...")
        continue