from random import randint

t = ["Rock", "Paper", "Scissors"]
computer = t[randint(0, 2)]

player = False

while player == False:
    player = input("Rock, Paper, Scissors?>>>")
    if computer == player:
        print("Tie")
    elif player == "Rock":
        if computer == "Scissors":
            print("You win!", player, "beats", computer)
        else:
            print("You lose!", computer, "beats", player)
    elif player == "Paper":
        if computer == "Rock":
            print("You win!", player, "beats", computer)
        else:
            print("You lose!", computer, "beats", player)
    elif player == "Scissors":
        if computer == "Paper":
            print("You win!", player, "beats", computer)
        else:
            print("You lose!", computer, "beats", player)
    else:
        print("Not and option. Check your spelling!")
    player = False
    computer = t[randint(0, 2)]
    