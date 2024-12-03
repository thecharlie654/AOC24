part_1 = 0
part_2 = 0

# Part 1

with open("input.txt") as f:
    reports = [i.strip().split(" ") for i in f]

def is_positive(n):
    if n > 0:
        return True
    else:
        return False

for i, report in enumerate(reports):
    report = [int(level) for level in report]
    diff = report[1]-report[0]
    trend = is_positive(diff)
    for j, level in enumerate(report[:-1]):
        diff = report[j+1]-report[j]
        trend_2 = is_positive(diff)
        if abs(diff) < 1 or abs(diff) > 3 or trend != trend_2:
            break
        if j == len(report[:-1])-1:
            part_1 += 1



# Part 2

with open("input.txt") as f:
    reports = [i.strip().split(" ") for i in f]

def check_if_safe(report):
    diff = report[1]-report[0]
    trend = is_positive(diff)
    for j, level in enumerate(report[:-1]):
        diff = report[j+1]-report[j]
        trend_2 = is_positive(diff)
        if abs(diff) < 1 or abs(diff) > 3 or trend != trend_2:
            return False
        if j == len(report[:-1])-1:
            return True

def problem_dampener(report):
    for i, level in enumerate(report):
        report_modified = report[:]
        report_modified.pop(i)
        if check_if_safe(report_modified):
            return True
    return False
        
for i, report in enumerate(reports):
    report = [int(level) for level in report]
    if check_if_safe(report):
        part_2 += 1
    else:
        if problem_dampener(report):
            part_2 += 1

print(f"{part_1=}")
print(f"{part_2=}")