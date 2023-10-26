import sys
import random

print(" ")
playerchoice = input("Enter..\n1 for rock,\n2 for paper,\n3 for sciccors:\n\n")

player = int(playerchoice)

if player < 1 | player | player > 3:
    sys.exit("you must enter 1 , 2 , or 3.")

    computerchoice = random.choice("123")

    computer = int(computerchoice)

    print("")
    print("you choose" + playerchoice + ".")
    print("python" + computerchoice + ".")
    print("")

    if player == 1 and computer == 3:
        print("you win")
    elif player == 2 and computer == 1:
        print("you win")
    elif player == 3 and computer == 2:
        print("you win")
    elif player == computer:
        print("tie game")
else:
    print("😒 python wins")
