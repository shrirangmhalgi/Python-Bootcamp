response = input("Hey how is it going...? ")
while True:
    # print(response)
    response = input(response + "\n")
    
    if response == "stop":
        print("You win...")
        break
