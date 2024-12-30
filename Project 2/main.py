from random import randint
n=randint(1,100)
number=-1
guesses=0
while (number!=n):
    guesses+=1
    number=int(input("Guess a number: "))

    if (number>n):
        print("Lower number please")
    else:
        print("Higher number please")

    
print(f"Yay!! You have successfully guessed the correct number in {guesses} attempts. ")