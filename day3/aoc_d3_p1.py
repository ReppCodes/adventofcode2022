import os
import string

input_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "input_p1.txt")

with open(input_path, "r") as fp:
    lines = fp.readlines()

allLetters = string.ascii_lowercase + string.ascii_uppercase

misplacedItems = []
for line in lines:
    packOne = line[0:len(line)//2]
    packTwo = line[len(line)//2:]
    for letter in packOne:
        if letter in packTwo:
            misplacedItems.append(letter)
            break

score = 0
for item in misplacedItems:
    score += (allLetters.find(item) + 1)

print(f"The summed priorities are: {score}")
