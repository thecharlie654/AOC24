# Part 1
import itertools

with open("input.txt") as f:
    lines = [i for i in f]
    for i, line in enumerate(lines):
        split_line = line.strip().split(":")
        split_line[0] = int(split_line[0])
        split_line[1] = split_line[1].strip().split(" ")
        split_line[1] = [int(i) for i in split_line[1]]
        lines[i] = split_line

def calculate_result(numbers, operator_combination):
    total = numbers[0]
    for i, operator in enumerate(operator_combination):
        if operator == "+":
            total += numbers[i+1]
        elif operator == "*":
            total *= numbers[i+1]
    return total

operators = ["+", "*"]
part_1 = 0
for equation in lines:
    test_value = equation[0]
    numbers = equation[1]
    operator_combinations = list(itertools.product(operators, repeat=len(numbers)-1))
    for operator_combination in operator_combinations:
        if calculate_result(numbers, operator_combination) == test_value:
            part_1 += test_value
            break

print(f"{part_1=}")

# Part 2
import itertools

with open("input.txt") as f:
    lines = [i for i in f]
    for i, line in enumerate(lines):
        split_line = line.strip().split(":")
        split_line[0] = int(split_line[0])
        split_line[1] = split_line[1].strip().split(" ")
        split_line[1] = [int(i) for i in split_line[1]]
        lines[i] = split_line

def calculate_result(numbers, operator_combination):
    total = numbers[0]
    for i, operator in enumerate(operator_combination):
        if operator == "+":
            total += numbers[i+1]
        elif operator == "*":
            total *= numbers[i+1]
        elif operator == "||":
            total = int(str(total) + str(numbers[i+1]))
    return total

operators = ["+", "*", "||"]
part_2 = 0
for equation in lines:
    test_value = equation[0]
    numbers = equation[1]
    operator_combinations = list(itertools.product(operators, repeat=len(numbers)-1))
    for operator_combination in operator_combinations:
        if calculate_result(numbers, operator_combination) == test_value:
            part_2 += test_value
            break

print(f"{part_2=}")