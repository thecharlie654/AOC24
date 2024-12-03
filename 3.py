import re
import time

# Part 1

with open("input.txt") as f:
    input_f = f.read()

search = re.findall(r'mul\(([0-9]+),([0-9]+)\)', input_f)

part_1 = 0
for pair in search:
    pair = list(map(int, pair))
    part_1 += int(pair[0]) * int(pair[1])

print(f"{part_1=}")

# Part 2

with open("input.txt") as f:
    input_f = f.read()

mul_search_indexes = re.finditer(r'mul\(([0-9]+),([0-9]+)\)', input_f)
mul_search = re.findall(r'mul\(([0-9]+),([0-9]+)\)', input_f)
enable_search = re.finditer(r'do\(\)', input_f)
disable_search = re.finditer(r'don\'t\(\)', input_f)
mul_indexes = [i.start() for i in mul_search_indexes]
enable_indexes = [i.start() for i in enable_search]
disable_indexes = [i.start() for i in disable_search]

enabled = True
part_2 = 0

for i in range(len(input_f)-1):
    # print(f"{i=}, {enabled=}")
    if i in enable_indexes:
        enabled = True
    if i in disable_indexes:
        enabled = False
    if i in mul_indexes and enabled:
        pair = mul_search[mul_indexes.index(i)]
        part_2 += int(pair[0]) * int(pair[1])

print(f"{part_2=}")