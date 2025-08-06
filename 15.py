# Part 1
import numpy as np

def find_robot_pos():
    for y, row in enumerate(warehouse_map):
        for x, character in enumerate(row):
            if character == "@":
                return [x, y]

def access_grid(x, y):
    if x > len(warehouse_map[0]) - 1:
        return None
    if y > len(warehouse_map) - 1:
        return None
    if x < 0 or y < 0:
        return None
    else:
        return warehouse_map[y][x]

def update_grid(vector, length_of_move, robot_pos):
    while length_of_move > 0:
        final_element_pos = np.add(robot_pos, np.multiply(vector, length_of_move - 1))
        new_location = np.add(final_element_pos, vector)
        warehouse_map[new_location[1]][new_location[0]] = access_grid(*final_element_pos)
        warehouse_map[final_element_pos[1]][final_element_pos[0]] = "."
        length_of_move -= 1

def attempt_move(vector):
    robot_pos = find_robot_pos()
    length_of_move = 0
    move_possible = False
    new_pos = np.add(robot_pos, vector)
    while move_possible is False:
        if access_grid(*new_pos) == ".":
            length_of_move += 1
            move_possible = True
        elif access_grid(*new_pos) == "O":
            new_pos = np.add(new_pos, vector)
            length_of_move += 1
        elif access_grid(*new_pos) == "#":
            return None
    update_grid(vector, length_of_move, robot_pos)

with open("input.txt") as f:
    input_f = f.read()

warehouse_map, instructions = input_f.split("\n\n")
warehouse_map = [list(row) for row in warehouse_map.split("\n")]
instructions = "".join([i.strip() for i in instructions])

for instruction in instructions:
    result = 0
    if instruction == ">":
        vector = [1, 0]
    elif instruction == "<":
        vector = [-1, 0]
    elif instruction == "^":
        vector = [0, -1]
    elif instruction == "v":
        vector = [0, 1]
    else:
        continue
    attempt_move(vector)

part_1 = 0

for y, row in enumerate(warehouse_map):
    for x, character in enumerate(row):
        if character == "O":
            part_1 += y * 100
            part_1 += x

print(f"{part_1=}")

# Part 2
import copy
def access_grid(x, y):
    if x > len(warehouse_map_modified[0]) - 1:
        return None
    if y > len(warehouse_map_modified) - 1:
        return None
    if x < 0 or y < 0:
        return None
    else:
        return warehouse_map_modified[y][x]

def find_robot_pos():
    for y, row in enumerate(warehouse_map_modified):
        for x, character in enumerate(row):
            if character == "@":
                return [x, y]

def attempt_move(vector, object_pos):
    new_pos = np.add(object_pos, vector)
    object_type = access_grid(*object_pos)
    obstacle = access_grid(*new_pos)
    if obstacle == "#":
        return None
    if obstacle == "[" or obstacle == "]":
        if obstacle == "[":
            other_half = np.add(new_pos, [1, 0])
        elif obstacle == "]":
            other_half = np.add(new_pos, [-1, 0])
        if attempt_move(vector, new_pos) is None:
            return None
        if vector[1] != 0:
            if attempt_move(vector, other_half) is None:
                return None
    x, y = new_pos
    warehouse_map_modified[y][x] = object_type
    x, y = object_pos
    warehouse_map_modified[y][x] = "."
    return True

with open("input.txt") as f:
    input_f = f.read()

warehouse_map, instructions = input_f.split("\n\n")
warehouse_map = [list(row) for row in warehouse_map.split("\n")]
instructions = "".join([i.strip() for i in instructions])

warehouse_map_modified = []
for row in warehouse_map:
    new_row = []
    for character in row:
        if character == "#":
            new_row.append("##")
        elif character == "O":
            new_row.append("[]")
        elif character == ".":
            new_row.append("..")
        elif character == "@":
            new_row.append("@.")
    warehouse_map_modified.append(list("".join(new_row)))

for instruction in instructions:
    if instruction == ">":
        vector = [1, 0]
    elif instruction == "<":
        vector = [-1, 0]
    elif instruction == "^":
        vector = [0, -1]
    elif instruction == "v":
        vector = [0, 1]
    else:
        continue
    robot_pos = find_robot_pos()
    warehouse_map_modified_backup = copy.deepcopy(warehouse_map_modified)
    if attempt_move(vector, robot_pos) is None:
        warehouse_map_modified = copy.deepcopy(warehouse_map_modified_backup)

print("\n".join(["".join(row) for row in warehouse_map_modified]))

part_2 = 0
for y, row in enumerate(warehouse_map_modified):
    for x, character in enumerate(row):
        if character == "[":
            part_2 += y * 100
            part_2 += x

print(f"{part_2=}")