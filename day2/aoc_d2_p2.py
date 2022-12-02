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
goalLose = "X"
goalDraw = "Y"
goalWin = "Z"

# helper functions
def scoreGame(opponentChoice, myGoal):
    score = 0
    if opponentChoice == opponentRock:
        if myGoal == goalLose:
            score += scissorsScore
            score += loseScore
        elif myGoal == goalDraw:
            score += rockScore
            score += drawScore
        elif myGoal == goalWin:
            score += paperScore
            score += winScore
    elif opponentChoice == opponentPaper:
        if myGoal == goalLose:
            score += rockScore
            score += loseScore
        elif myGoal == goalDraw:
            score += paperScore
            score += drawScore
        elif myGoal == goalWin:
            score += scissorsScore
            score += winScore
    elif opponentChoice == opponentScissors:
        if myGoal == goalLose:
            score += paperScore
            score += loseScore
        elif myGoal == goalDraw:
            score += scissorsScore
            score += drawScore
        elif myGoal == goalWin:
            score += rockScore
            score += winScore
    return score


# process lines
runningScore = 0
for line in lines:
    opponentChoice, myGoal = line.rstrip().split(" ")
    runningScore += scoreGame(opponentChoice=opponentChoice, myGoal=myGoal)

print(f"Score of this guide is: {runningScore}")
# Score of this guide is: 12429
