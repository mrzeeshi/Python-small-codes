#------------------------In this file we will deal with the functions-------------------
def greet(name):
    print("Hello ",name," How are you?")
greet("Zeeshan")

#-------------------function for checking a number whether it is prime or not------------------------
def is_prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True

    count = 2
    while count * count <= number:
        if number % count == 0:
            return False
        count += 1

    return True


if is_prime(3):
    print("Prime number")
else:
    print("Not a prime number")


#--------------Finding the factorial of a number-------------
def factorial(val):
    i=val
    factoriall=1
    while i>=1:
        factoriall*=i
        i-=1
    return factoriall
print(factorial(4))


#----------------Finding the factorial using the recursive funtion
def recursive_factorial(val):
    if val == 0 or val == 1:
        return 1
    else:
        return val * recursive_factorial(val - 1)

print(recursive_factorial(4))

#--------------------Filtering a list to find the even numbers--------------------
def filter_list(vals):
    evans=[]
    for val in vals:
        if val%2==0:
            evans.append(val)
    return evans
check_evan_vals=[1,2,4,7,9,6,8,3,5]
evan_vals=filter_list(check_evan_vals)
print(evan_vals)


#----------------Vowel counter in a sentence-----------------#
def vowel_counter(sentence):
    vowels=['a','e','i','o','u']
    vowels_count=0
    for char in sentence:
        if char in vowels:
            vowels_count+=1
    return vowels_count
s=str(input("Enter the sentence for which you want to count the vowels"))
print("There are ",vowel_counter(s)," vowels in the sentence you provided")

#-------------Palindrome check for a complete sentence---------------#
def is_palindrome(enter_whatever_you_want_to_check_the_palindrome_for):
    clean_text=enter_whatever_you_want_to_check_the_palindrome_for.replace(" ","")
    reversed_sentence=""
    for char in clean_text:
        reversed_sentence=char+reversed_sentence
    if reversed_sentence==clean_text:
        return True
    else:
        return False
check_palindrome=str(input("Enter any sentence or word for which you want to check the palindrome for"))
if is_palindrome(check_palindrome):
    print(check_palindrome," is a palindrome sentence.")
else:
    print(check_palindrome," is not a palindrome sentence.")