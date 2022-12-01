import os

input_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "input_p2.txt")

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


elves.sort(reverse=True)
result = elves[0] + elves[1] + elves[2]
print(f"Elf with the most has: {result}")
# Right answer is: 203905
