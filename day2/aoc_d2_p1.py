import os

input_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "input_p1.txt")

with open(input_path, "r") as fp:
    lines = fp.readlines()


# Defined vars in prompt
rockScore = 1
paperScore = 2
scissorsScore = 3
loseScore = 0
drawScore = 3
winScore = 6
opponentRock = "A"
opponentPaper = "B"
opponentScissors = "C"
myRock = "X"
myPaper = "Y"
myScissors = "Z"

# helper functions
def scoreGame(opponentChoice, myChoice):
    score = 0
    if opponentChoice == opponentRock:
        if myChoice == myRock:
            score += rockScore
            score += drawScore
        elif myChoice == myPaper:
            score += paperScore
            score += winScore
        elif myChoice == myScissors:
            score += scissorsScore
            score += loseScore
    elif opponentChoice == opponentPaper:
        if myChoice == myRock:
            score += rockScore
            score += loseScore
        elif myChoice == myPaper:
            score += paperScore
            score += drawScore
        elif myChoice == myScissors:
            score += scissorsScore
            score += winScore
    elif opponentChoice == opponentScissors:
        if myChoice == myRock:
            score += rockScore
            score += winScore
        elif myChoice == myPaper:
            score += paperScore
            score += loseScore
        elif myChoice == myScissors:
            score += scissorsScore
            score += drawScore
    
    return score


# process lines
runningScore = 0
for line in lines:
    opponentChoice, myChoice = line.rstrip().split(" ")
    runningScore += scoreGame(opponentChoice=opponentChoice, myChoice=myChoice)

print(f"Score of this guide is: {runningScore}")
# Score of this guide is: 9759
