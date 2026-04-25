#As i am practicing here about the classes so there are two to three different classes.So in order to test each class you have to comment out others
#There also exists a mini project whose class is Coffee_shop at last
#To run that project comment out the other obove two classes otherwise there will be messy output
#Keep in mind the above instructions
class dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def bark(self):
        print(self.name+" says woof and has an age = ",self.age)
d1=dog("Tommy",8)
d1.bark()



class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def increase_salary(self):
        self.salary+=(self.salary/100)*10
        print("The salary was increased and the new salary is = ",self.salary)
e1=employee("zeeshan",14000)
e1.increase_salary()

class student_marks:
    def __init__(self,marks1,marks2,marks3):
        self.marks1=marks1
        self.marks2=marks2
        self.marks3=marks3
    def calculate_average_marks(self):
        print((self.marks1+self.marks2+self.marks3)/3)
marks1=student_marks(14,54,76)
marks1.calculate_average_marks()
  
class Coffee_shop:
    def __init__(self,bill=0,orders=[]):
        self.bill=bill
        self.orders=orders
    def order_coffee(self):
        self.orders.append("1.Coffee....................40$.")
        self.bill+=40
    def order_cookies(self):
        self.orders.append("2.Cookies...................30$.")
        self.bill+=30
    def order_hotmilk(self):
        self.orders.append("3.Hot Milk..................50$.")
        self.bill+=50
    def show_bill(self):
        print("===============BILL==============")
        print("Item........................Price")
        for i in range(len(self.orders)):
            print(self.orders[i])
        print("Total.......................=",self.bill,"$")
print("==================================")
print("||      Zeeshi Coffee Shop      ||")
print("==================================")
print("==============WELCOME=============")
print("==================================")
getting_orders=True
o1=Coffee_shop()
while getting_orders:
    print("===============MANUE==============")
    print("Item.........................Price")
    print("1.Coffee......................40$.")
    print("2.Cookies.....................30$.")
    print("3.Hot Milk....................50$.")
    print("=========Press 0 To Exit==========")
    choice=int(input("Select the resptive number for each order::"))
    if choice>3 and choice<0:
        print("Invalid Choice!!!Choose between 0 and 3 as above mentioned...")
        continue
    else:
        if choice==1:
            o1.order_coffee()
            continue
        elif choice==2:
            o1.order_cookies()
        elif choice==3:
            o1.order_hotmilk()
        else:
            o1.show_bill()
            getting_orders=False