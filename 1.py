# Part 1

left = []
right = []

with open("input.txt") as f:
    for line in f:
        split_line = line.strip("\n").split("   ")
        left.append(split_line[0])
        right.append(split_line[1])

left = [int(i) for i in left]
right = [int(i) for i in right]

left.sort()
right.sort()

part_1 = 0
for i, num1 in enumerate(left):
    diff = abs(num1 - right[i])
    part_1 += diff

print(f"{part_1=}")

# Part 2

left = []
right = []

with open("input.txt") as f:
    for line in f:
        split_line = line.strip("\n").split("   ")
        left.append(split_line[0])
        right.append(split_line[1])

left = [int(i) for i in left]
right = [int(i) for i in right]

left.sort()
right.sort()

part_2 = 0
for num1 in left:
    part_2 += num1 * right.count(num1)

print(f"{part_2=}")
