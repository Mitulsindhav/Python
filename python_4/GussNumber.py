import random

num=random.randint(1,20)

while True:

    guess=int(input("Guess Number Beetween 1 TO 20 :"))
    if guess==num:
        print("You are Guessed A correct Number")
        break
    elif guess>num:
        print("You are a Greater Number")
    elif guess<num:
        print("You are a Smaller Number")

        


