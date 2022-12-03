import os
import string

input_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "input_p1.txt")

with open(input_path, "r") as fp:
    lines = fp.readlines()

allLetters = string.ascii_lowercase + string.ascii_uppercase

groups = []
for i in range(0, len(lines), 3):
    groups.append(lines[i:i+3])

badges = []
for group in groups:
    for item in group[0]:
        if item in group[1] and item in group[2]:
            badges.append(item)
            break

score = 0
for badge in badges:
    score += (allLetters.find(badge) + 1)

print(f"The summed badge priorities are: {score}")
