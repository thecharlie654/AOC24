import re
import time

with open("input.txt") as f:
    input_f = f.read()

search = re.findall(r'mul\(([0-9]+),([0-9]+)\)', input_f)

part_1 = 0
for pair in search:
    pair = list(map(int, pair))
    part_1 += int(pair[0]) * int(pair[1])

print(f"{part_1=}")