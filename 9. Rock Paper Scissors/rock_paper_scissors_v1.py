while True:
    print("\n...Rocks...")
    print("...Papers...")
    print("...Scissors...")
    print("...-1 to exit...")

    player1_input = input("Player 1 enter your choice... : ")
    print("\n" * 20) #you can repeat something n number of times by giving multiplication sign

    if player1_input == "-1" :
        quit();

    player2_input = input("Player 2 enter your choice... :")

    if player1_input == "scissors" :
        if player2_input == "papers" :
            print("Player 1 wins...")
        elif player2_input == "rocks" :
            print("Player 2 wins...")
        else :
            print("Its a draw...")

    elif player1_input == "rocks" :
        if player2_input == "scissors" :
            print("Player 1 wins...")
        elif player2_input == "papers" :
            print("Player 2 wins...")
        else :
            print("Its a draw...")

    else :
        if player2_input == "rocks" :
            print("Player 1 wins...")
        elif player2_input == "scissors" :
            print("Player 2 wins...")
        else :
            print("Its a draw...")
    
    print("\n")
