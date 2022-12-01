import os

input_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "input_p1.txt")

with open(input_path, "r") as fp:
    lines = fp.readlines()

elves = []
calcounter = 0
for line in lines:
    if line == "" or line == "\n":
        elves.append(calcounter)
        calcounter = 0
    else:
        calcounter += int(line)

print(f"Elf with the most has: {max(elves)}")
