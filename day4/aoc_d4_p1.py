import os
import string

input_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "input_p1.txt")

with open(input_path, "r") as fp:
    lines = fp.readlines()

def parseItems(dashrange):
    start, stop = dashrange.split("-")
    return set(range(int(start),int(stop)+1))

score = 0
for line in lines:
    elfOne, elfTwo = line.split(",")
    elfOneItems = parseItems(elfOne)
    elfTwoItems = parseItems(elfTwo)

    if elfOneItems.issuperset(elfTwoItems) or elfTwoItems.issuperset(elfOneItems):
        score += 1

print(f"The number of useless elves is: {score}")