"""
# METHOD 01: read file
f=open("funny.txt","r")
for line in f:
    print(line)
f.close()

# METHOD 02: read lines
f=open("funny.txt","r")
lines=f.readlines()
f.close()


# METHOD 03: use append to stop having previous lines overwritten
f=open("love.txt","a")
f.write("\nI love python")
f.close()


# METHOD 04: write lines     
f=open("love.txt","w")
f.writelines(["I love python"])
f.close()


# same file when we write I love javascript the previous line goes away
f=open("love.txt","w")
f.write("I love javascript")
f.close()



# METHOD 05: with statement
with open("funny.txt","r") as f:
    for line in f:
        print(line)
"""

# https://www.cricketworldcup.com/teams/india/players/107

player_scores={}


with open("scores.csv","r") as f:
    for line in f:
        token=line.split(",")
        player=token[0]
        score=int(token[1])
        if player in player_scores:
            player_scores[player].append(score)
        else:
            player_scores[player]=[score]

for player, score_list in player_scores.items():
    min_score=min(score_list)
    max_score=max(score_list)
    avg_score=sum(score_list)/len(score_list)

    print(f"{player}==> Minimum score: {min_score}, Maximum score: {max_score}, Average score: {avg_score} ")
        