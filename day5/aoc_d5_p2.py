import os
import string
import re

input_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "input_p1.txt")

with open(input_path, "r") as fp:
    lines = fp.read()

stacks, moves = lines.split("\n\n")
moveLines = moves.split("\n")

# parse stacks into list of lists
cargo = []
currStacks = []
numstacks = 0
for line in stacks.split("\n"):
    if line.startswith(" 1"):
        numstacks = int(line.strip()[-1])
    else:
        line = line.replace("    ", "[]").strip().split("]")
        currStacks.append(line)

for idx in range(numstacks):
    cargo.append([])

for line in currStacks:
    for idx, stack in enumerate(line):
        stack = stack.replace("[","").strip()
        if stack:
            cargo[idx].append(stack)

for stack in cargo:
    stack.reverse()

# parse move lines
for line in moveLines:
    num = re.findall(r'\d+', line) 
    numMoved = int(num[0])
    source = int(num[1])
    dest = int(num[2])
    crate = cargo[source-1][-numMoved:]
    cargo[dest-1].extend(crate)
    cargo[source-1] = cargo[source-1][:-numMoved]

result = ""
for stack in cargo:
    result += stack[-1]

print(f"The crates on the top of the stack are: {''.join(result)}")
