#----------------------In this file you will see the coding problems related to  loops----------------------
#1.printing the natural numbers from 0 to 10
# for i in range(11):
#     print (i)

#2.prnting all the prime and non prime numbers from 1 to 100
# for i in range(100):
#     count=2
#     is_prime=True
#     if i<=1:
#         continue;
#     else:
#         while count*count<=i:
#         # #(this line is written because it will check untill the square root of the number 
#         #     for we are checking the prime)
#             if i%count==0:
#                 is_prime=False
#                 break;
#             else:
#                 count+=1
#     if is_prime==True:
#         print(i," is prime number!")
#     else:
#         print(i," is not a prime number!")

#3.Patterns-----------------------------------
# *
# **
# ***
# ****
# *****

for i in range(5):
    print("*"*(i+1))


#     *
#    ***
#   *****
#  *******
# *********

rows = 5
cols = 1

for i in range(rows):
    print(" " * (rows - i), "*" * cols, sep="")
    cols += 2

#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *
rows = 5
cols = 1

for i in range(rows):
    print(" " * (rows - i), "*" * cols, sep="")
    cols += 2
for i in range(rows):
    print(" " *(i),"*" * (cols), sep="")
    cols -= 2