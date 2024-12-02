left = []
right = []

with open("input.txt") as f:
    for line in f:
        split_line = line.strip("\n").split("   ")
        left.append(split_line[0])
        right.append(split_line[1])

left = [int(i) for i in left]
right = [int(i) for i in right]

# Part 1
# left.sort()
# right.sort()
#
# sum = 0
# for i, num1 in enumerate(left):
#     diff = abs(num1 - right[i])
#     sum += diff
#
# print(sum)

# Part 2

sum = 0
for num1 in left:
    sum += num1 * right.count(num1)

print(sum)
