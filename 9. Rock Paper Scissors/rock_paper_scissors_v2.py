import random

while True:
    print("\n...Rocks...")
    print("...Papers...")
    print("...Scissors...")
    print("...-1 to exit...")

    player_input = input("Player enter your choice... : ").lower()

    if player_input == "-1" :
        quit();

    computer_input = random.randint(1, 3)
    if(computer_input == 1) :
        computer_input = "rocks"
    elif(computer_input == 2) :
        computer_input = "papers"
    else :
        computer_input = "scissors"

    print("Computer played... : " + computer_input)

    if player_input == computer_input :
        print("Its a draw")
    elif player_input == "scissors" :
        if computer_input == "papers" :
            print("You win...")
        else :
            print("Computer wins...")
    elif player_input == "rocks" :
        if computer_input == "scissors" :
            print("You Win...")
        else :
            print("Computer wins...")
    else :
        if computer_input == "rocks" :
            print("You win...")
        else :
            print("Computer wins...")
    
    print("\n")
