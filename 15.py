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
        # print(f"{final_element_pos=}")
        new_location = np.add(final_element_pos, vector)
        # print(f"{new_location=}")
        warehouse_map[new_location[1]][new_location[0]] = access_grid(*final_element_pos)
        warehouse_map[final_element_pos[1]][final_element_pos[0]] = "."
        length_of_move -= 1


def attempt_move(vector):
    robot_pos = find_robot_pos()
    length_of_move = 0
    move_possible = False
    new_pos = np.add(robot_pos, vector)
    # print(f"{access_grid(*new_pos)=}")
    while move_possible is False:
        if access_grid(*new_pos) == ".":
            length_of_move += 1
            move_possible = True
        elif access_grid(*new_pos) == "O":
            new_pos = np.add(new_pos, vector)
            length_of_move += 1
        elif access_grid(*new_pos) == "#":
            return None
    # print(length_of_move, vector)
    update_grid(vector, length_of_move, robot_pos)
    

with open("input.txt") as f:
    input_f = f.read()

warehouse_map, instructions = input_f.split("\n\n")
warehouse_map = [list(row) for row in warehouse_map.split("\n")]

for instruction in instructions:
    print(instruction)
    if instruction == ">":
        vector = [1, 0]
        print("Attempting to move right")
    elif instruction == "<":
        vector = [-1, 0]
        print("Attempting to move left")
    elif instruction == "^":
        vector = [0, -1]
        print("Attempting to move up")
    elif instruction == "v":
        vector = [0, 1]
        print("Attempting to move down")
    # print(f"Move length for instruction {instruction} is {attempt_move(vector)}")
    # print(f"{instruction=}")
    attempt_move(vector)
    input()
    for row in warehouse_map:
        print("".join(row))

part_1 = 0

for y, row in enumerate(warehouse_map):
    for x, character in enumerate(row):
        if character == "O":
            part_1 += y * 100
            part_1 += x

print(f"{part_1=}")