with open("input.txt") as f:
    reports = [i.strip().split(" ") for i in f]

def is_positive(n):
    if n > 0:
        return True
    else:
        return False

sum = 0

# Part 1
#
# for i, report in enumerate(reports):
#     problems = 0
#     report = [int(level) for level in report]
#     diff = report[1]-report[0]
#     trend = is_positive(diff)
#     for j, level in enumerate(report[:-1]):
#         diff = report[j+1]-report[j]
#         trend_2 = is_positive(diff)
#         if abs(diff) < 1 or abs(diff) > 3 or trend != trend_2:
#             break
#         if j == len(report[:-1])-1:
#             sum += 1

# Part 2
for i, report in enumerate(reports):
    problems = 0
    report = [int(level) for level in report]
    diff = report[1]-report[0]
    trend = is_positive(diff)
    for j, level in enumerate(report[:-1]):
        diff = report[j+1]-report[j]
        trend_2 = is_positive(diff)
        if abs(diff) < 1 or abs(diff) > 3 or trend != trend_2:
            break
        if j == len(report[:-1])-1:
            sum += 1

print(sum)