"""
1 for Snake
2 for Water 
3 for Gun

"""

import random 
ComputerChoice=random.choice([1,2,3])
YourChoice=input("Enter your choice(S/W/G): ")
YourDict={"S":1,"W":2, "G":3}
ReverseDict={1:"Snake",2:"Water",3:"Gun"}

You=YourDict[YourChoice]
print(f"You chose {ReverseDict[You]}")
print(f"Computer chose {ReverseDict[ComputerChoice]}")

if (ComputerChoice==You):
    print("It's a draw.")

else:
    if (You==1 and ComputerChoice==2):
        print("You win!")
    elif (You==2 and ComputerChoice==3):
        print("You win!")
    elif (You==3 and ComputerChoice==1):
        print("You win!")
    elif (You==1 and ComputerChoice==3): 
        print("You Lose!\n" "Better luck next time.")
    elif (You==2 and ComputerChoice==1):
        print("You Lose!\n" "Better luck next time.")
    elif (You==3 and ComputerChoice==2):
        print("You Lose!\n" "Better luck next time.")
    else:
        print("An error occured.")
    
