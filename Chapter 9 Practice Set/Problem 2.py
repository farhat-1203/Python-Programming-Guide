import random

def game():
    print("Your are playing the game")
    score=random.randint(1,62)
    # Fetch the hiscore
    with open("Hi-score.txt") as f:
        hiscore=f.read()
        if (hiscore!==""):
            hiscore=int(hiscore)
        else:
            hiscore=0

        print(f "Your score: {score}")
        if (score>int(hiscore) or hiscore==" "):
            # write this hi-score to the file
            with open("Hi-score.txt", "w") as f:
                f.write(str(score))
        return score

    
game()