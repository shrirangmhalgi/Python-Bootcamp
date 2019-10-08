import random

while True :
    number = random.randint(1, 10)
    guess = int(input("Enter a number... : "))

    while guess != number :
        if guess < number :
            print("too low...")
            guess = int(input("Enter a number... : "))
        elif guess > number :
            print("too high...")
            guess = int(input("Enter a number... : "))
    
    print("You guessed it...")
    choice = input("Do you want to play again...? : ")
    if choice == "y" :
        continue
    else :
        print("thanks for playing...")
        break