import os
from collections import defaultdict
import re

input_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "input_p1.txt")
with open(input_path, "r") as fp:
    lines = fp.readlines()

dirs = {}
currTree = []
dirSize = defaultdict(lambda: 0)
for line in lines:
    if line == "$ cd /":
        currTree = ["/"]
    elif line.startswith("dir"):
        continue
    elif line.startswith("$ cd .."):
        currTree.pop()
    elif line.startswith("$ cd"):
        newDir = line.replace("$ cd ","").strip()
        currTree.append(newDir)
    elif re.match(r'^\d+', line):
        fileSize = int(re.findall(r'^\d+', line)[0])
        for idx, _ in enumerate(currTree):
            fullPath = '/'.join(currTree[:idx+1])
            dirSize[fullPath] += fileSize

score = 0
for dir in dirSize:
    blockSize = dirSize.get(dir)
    if blockSize <= 100000:
        score += blockSize

print(f"Total block size of small dirs is: {score}")