import os
import heapq

input_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "input_p1.txt")

with open(input_path, "r") as fp:
    stream = fp.read()

trailingVals = []
marker = None
for idx, char in enumerate(stream):
    if len(trailingVals) < 14:
        heapq.heappush(trailingVals, (idx, char))
    else:
        heapq.heapreplace(trailingVals, (idx, char))

    values = set([x[1] for x in trailingVals])
    if len(values) == 14:
        marker = idx+1
        break

print(trailingVals)
print(f"The data stream begins at: {marker}")