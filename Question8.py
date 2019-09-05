print("Please make your choice")
print("Enter 1 for rock\nEnter 2 for scissors\nEnter 3 for paper")

while True:
    player1 = int(input("Player 1 enter your choice: "))
    player2 = int(input("Player 2 enter your choice: "))
    if player1 == 1 or player1 == 2 or player1 == 3:
        if player2 == 1 or player2 == 2 or player2 == 3:
            if player1 == player2:
                print("Same choice")

            elif player1 == 1:
                if player2 == 2:
                    print("Congratulation to player 1")
                else:
                    print("Congratulation to player 2")
            elif player1 == 2:
                if player2 == 3:
                    print("Congratulation to player 1")
                else:
                    print("Congratulation to player 2")
            elif player1 == 3:
                if player2 == 1:
                    print("Congratulation player 1")
                else:
                    print("Congratulation player 2")

        else:
            print("Please enter the right choice")
    else:
        print("Please enter the right choice")

    print("Do you want to start a new game?")
    choice = int(input("Enter 1 to restart or Enter 2 to end the program: "))
    if choice == 2:
        print("You have exit the program")
        break
    else:
        True
