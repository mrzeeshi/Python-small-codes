import random
print("="*15,"Welcome to number guessing game","="*15)
number=random.randint(1,100)
not_guessed=True
count=0
while not_guessed:
    guess=int(input("Guess the number!!!"))
    count+=1
    if guess==number:
        print("Yo buddy you made it at ",count,"th attempt!!")
        not_guessed=False
    else:
        if guess>number:
            if guess-number<=10:
                print("You are near but higher than guess")
            else:
                print("Guessed a higher number")
        else:
            if number-guess<=10:
                print("you are near but below the guess")
            else:
                print("Guessed too low number")
    