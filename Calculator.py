# Hey,whatsupp guys!Hope you are doing well.This is the calculator that is similar to a scientific calculator but just doing the basic operations like the 
# additon subtraction multiplication and the division.As you know I am a beginner strugling to learn the things.
# INSTRUCTONS!!!
# 1.You have to enter a value then press enter
# 2.Then it will ask you for the operator like -,+,* and / for division(keep in mind)
# 3.Then enter the next value
# 4.The same process is repeated untill you press = to get the answer which allows you to solve a many values based on DMASS rule
# 5.Don't use the brackets or anything else than the operator or numbers coz it will give error
# 6.No error handling!!!
# 7.ENJOYYYYYYYYYYYYYYYYY!


def add(a,b):
    return a+b

def multiply(a,b):
    return a*b

def subtract(a,b):
    return a-b

def divide(a,b):
    return a/b


print("||============================================||")
print("||                                            ||")
print("||============================================||")
print("|| Scientific Calculator               on/off ||")
print("||--------------------------------------------||")
print("||    9    ||   10     ||     100    ||   /   ||")
print("||    6    ||    7     ||      8     ||   *   ||")
print("||    3    ||    4     ||      5     ||   -   ||")
print("||    0    ||    1     ||      2     ||   +   ||")
print("||--------------------------------------------||")
print("================================================")
taken=[]
getting_input=True

while getting_input:
    val=float(input("Enter the value :"))   
    operator=input("Enter the operator(press = to get the answer):")
    
    taken.append(val)
    
    if operator=="=":
        getting_input=False
    else:
        taken.append(operator)

while len(taken) > 1:

    if "/" in taken:
        div_index = taken.index("/")
        first_val = taken[div_index-1]
        second_val = taken[div_index+1]

        ans = divide(first_val, second_val)
        taken[div_index-1:div_index+2] = [ans]
        continue

    elif "*" in taken:
        mul_index = taken.index("*")
        first_val = taken[mul_index-1]
        second_val = taken[mul_index+1]

        ans = multiply(first_val, second_val)

        taken[mul_index-1:mul_index+2] = [ans]
        continue

    elif "-" in taken:
        sub_index = taken.index("-")
        first_val = taken[sub_index-1]
        second_val = taken[sub_index+1]

        ans = subtract(first_val, second_val)

        taken[sub_index-1:sub_index+2] = [ans]
        continue

    elif "+" in taken:
        sum_index = taken.index("+")
        first_val = taken[sum_index-1]
        second_val = taken[sum_index+1]

        ans = add(first_val, second_val)

        taken[sum_index-1:sum_index+2] = [ans]
        continue
print("Answer:", taken[0])