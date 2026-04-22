#----------------------In this file you will see the coding problems related to  loops----------------------
#1.printing the natural numbers from 0 to 10
# for i in range(11):
#     print (i)

#2.prnting all the prime and non prime numbers from 1 to 100
for i in range(100):
    count=2
    is_prime=True
    if i<=1:
        continue;
    else:
        while count*count<=i:
        # #(this line is written because it will check untill the square root of the number 
        #     for we are checking the prime)
            if i%count==0:
                is_prime=False
                break;
            else:
                count+=1
    if is_prime==True:
        print(i," is prime number!")
    else:
        print(i," is not a prime number!")

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

#Largest and smallest in a list using loop
numbers=[3,4,6,4,3,6,7,8654,3,3,5]
largest=numbers[0]
smallest=numbers[0]
for i in range(len(numbers)):
    if numbers[i]>largest:
        largest=numbers[i]
    elif numbers[i]<smallest:
        smallest=numbers[i]
print("Largest Number: ",largest)
print("Smallest Number: ",smallest)


# #Finding the count of each character in a word 
word=input("enter the word to find count of each character")
visited=[]
for alphabet in word:
    word_count=0
    if alphabet in visited:
        continue;
    else:
        visited.append(alphabet)
        for char in word:
            if char==alphabet:
                word_count+=1
        print("count of the ",alphabet," in ",word," you provided is ",word_count)

# ---printing the floyd triangle-------------
# 1
# 23
# 456
# 78910
# 1112131415
rows=5
counter=1
for row in range(rows):
    col=0
    while col<=row:
        print(counter,end="")
        counter+=1
        col+=1
    print()
