# Part 1

with open("input.txt") as f:
    input_f = [list(line.strip()) for line in f]

def get_map_item(x, y):
    if x < 0 or y < 0:
        return None
    if x > len(input_f[0])-1 or y > len(input_f)-1:
        return None
    return input_f[y][x]

def get_guard_position(input):
    for y, line in enumerate(input):
        for x, letter in enumerate(line):
            if letter in directions:
                return (x, y)

def get_guard_direction(input, x, y):
    letter = input[y][x]
    if letter == "^":
        return (0, -1)
    if letter == "v":
        return (0, 1)
    if letter == "<":
        return (-1, 0)
    if letter == ">":
        return (1, 0)

directions = ["^", ">", "v", "<"]

x, y = get_guard_position(input_f)
while True:
    guard_char = get_map_item(x, y)
    dx, dy = get_guard_direction(input_f, x, y)
    next_char = get_map_item(x+dx, y+dy)
    if next_char == None:
        input_f[y][x] = "X"
        break
    elif next_char == "#":
        new_direction_index = (directions.index(guard_char) + 1) % 4
        input_f[y][x] = directions[new_direction_index]
    else:
        input_f[y][x] = "X"
        input_f[y+dy][x+dx] = guard_char
        x = x+dx
        y = y+dy

part_1 = 0
for line in input_f:
    part_1 += line.count("X")

print(f"{part_1=}")

# Part 2

import copy

with open("input.txt") as f:
    input_f = [list(line.strip()) for line in f]

def get_map_item(x, y, input):
    if x < 0 or y < 0:
        return None
    if x > len(input[0])-1 or y > len(input)-1:
        return None
    return input[y][x]

def get_guard_position(input):
    for y, line in enumerate(input):
        for x, letter in enumerate(line):
            if letter in directions:
                return (x, y)

def get_guard_direction(input, x, y):
    letter = input[y][x]
    if letter == "^":
        return (0, -1)
    if letter == "v":
        return (0, 1)
    if letter == "<":
        return (-1, 0)
    if letter == ">":
        return (1, 0)

directions = ["^", ">", "v", "<"]

def check_loops(input):
    visited_coords = [[[] for i in range(len(input[0]))] for i in range(len(input))]
    x, y = get_guard_position(input)
    while True:
        guard_char = get_map_item(x, y, input)
        if guard_char in visited_coords[y][x]:
            return True
        visited_coords[y][x].append(guard_char)
        dx, dy = get_guard_direction(input, x, y)
        next_char = get_map_item(x+dx, y+dy, input)
        if next_char == None:
            input[y][x] = "X"
            return False
        elif next_char == "#":
            new_direction_index = (directions.index(guard_char) + 1) % 4
            input[y][x] = directions[new_direction_index]
        else:
            input[y][x] = "X"
            input[y+dy][x+dx] = guard_char
            x = x+dx
            y = y+dy

part_2 = 0
for y, line in enumerate(input_f):
    for x, letter in enumerate(line):
        if letter == ".":
            input_modified = copy.deepcopy(input_f)
            input_modified[y][x] = "#"
            if check_loops(input_modified):
                part_2 += 1

print(f"{part_2=}")

