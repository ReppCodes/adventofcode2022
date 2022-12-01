import os
import heapq

input_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "input_p2.txt")

with open(input_path, "r") as fp:
    lines = fp.readlines()


elves = []
calcounter = 0
for idx in range(len(lines)):
    line = lines[idx]
    if line == "" or line == "\n" or idx == len(lines)-1:
        if len(elves) < 3:
            heapq.heappush(elves, calcounter)
        else:
            minval = heapq.heappop(elves)
            heapq.heappush(elves, max(minval, calcounter))

        calcounter = 0
    else:
        calcounter += int(line)

print(f"Top 3 elves with the most has: {sum(elves)}")

