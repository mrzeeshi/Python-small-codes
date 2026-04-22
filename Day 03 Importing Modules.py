#-------------------------Here in this file we are going to learn about importing modules in python-------------------------
import math
import random
import datetime

#----------------------------random module-----------------------------------
#sqrt method takes the square root
print(math.sqrt(4))
#floor method coverts a decimal to whole number to down like converts 5.2 --> 5
print(math.floor(5.2))
#ceil method converts the float to wholw number to up like converts 5.2 ----->6
print(math.ceil(5.2))
#power used to give the powers
print(math.pow(2,3))
#pi method is used to find the power of pi
print(math.pi)
#-------------------------------random module--------------------------
print("choosing a random number between 1-10 -->",random.randint(1,10))
print("choosing a random float between 0-1-->",random.random())

#-------------------------------the date time module---------------------
print("the current date and time is :",datetime.datetime.now())
print("what is the day today---->",datetime.date.today())
#lets make the age calculater using this date and time
day=int(input("What was the day at which you were born:"))
month=int(input("What was the month of your birth:"))
year=int(input("What is the year of your birth:"))
now=datetime.datetime.now()
current_day=now.day
current_month=now.month
current_year=now.year
if current_day<day:
    current_month-=1
    current_day+=30
    days=current_day-day
else:
    days=current_day-day
if current_month<month:
    current_year-=1
    current_month+=12
    months=current_month-month
else:
    months=current_month-month
print("Your age is ",(current_year-year)," years ",months," months and ",days," days long, May you live 100 more years!")

