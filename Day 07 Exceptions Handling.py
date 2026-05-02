# # Just imagine you write a thousand lines of code and due to a small error your complete program crashes.
# # To solve this issue there comes the concept of exceptions handling.
# # By exceptions handling we tell the computer that we were expecting that error so if that error comes print this message and move on
# # There are the three main types of exceptions handled below

# # 1.ZeroDivisionError
# try:
#     a =int(input("enter the first number."))
#     b=int(input("enter the second number."))
#     print(a/b)
# except ZeroDivisionError:
#     print("You can't devide a number by zero...")

# # 2.ValueError
# try:
#     num=int(input("enter the number"))
#     if (num%2==0):
#         print("even number...")
#     else:
#         print("odd number...")
# except ValueError:
#     print("you must enter the number but not a string or a special character...")
  
# #  3.FileNotFoundError
# try:
#     file=open("a.txt","r")
#     file.read()
#     file.close()
# except FileNotFoundError:
#     print("the file you are trying to read does't exist...")

# # There are the some specific keywords that are used here and they are given below
# # 1.try:
# #     contains the code that might give the error
# # 2.except:
# #     returns and prints the specific exception if error haappens in the try code
# # 3.else
# #     if no error happens this code will run
# # 4.finally
# #     no matter exeption accurs or not this code will run

try:
    num1=int(input("enter the first number"))
    num2=int(input("enter the second number"))
    print("ans",num1/num2)
except Exception as e:
    print("this exception happened ",e)
else:
    print("the code ran successfully without any errors")
finally:
    print("done...")

# # We can also make our own exceptions like below I will try to make an exception named as lowage Exception
class LowAgeException(Exception):
    pass

try:
    age = int(input("Enter your age: "))
    
    if age < 18:
        raise LowAgeException("You are under 18")
    
    print("You are an adult")

except LowAgeException as e:
    print(e)