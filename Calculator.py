def add(a,b):
    return a+b
def multiply(a,b):
    return a*b
def subtract(a,b):
    return a-b
def divide(a,b):
    return a/b
print("=======================================Simple and basic calculator:===================================")
val1=int(input("Enter the first value:"))
operator=str(input("Enter the operator means what you want to do write like +,-,* or /:"))
val2=int(input("Enter the second value:"))
ans=0
if operator=="+":
    ans=add(val1,val2)
elif operator=="-":
    ans=subtract(val1,val2)
elif operator=="*":
    ans=multiply(val1,val2)
elif operator=="/":
    ans=divide(val1,val2)
else:
    print("You have chosen an invalid operator...")
print("Your answer is = " ,ans)