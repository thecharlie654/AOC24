with open("input.txt") as f:
    line = f.read().strip()

def get_free_pointer(formatted_map, previous_pointer):
    for i in range(map_length-previous_pointer):
        if formatted_map[i+previous_pointer] == ".":
            return i+previous_pointer
    return -1

formatted_map = []
file = True
for i, char in enumerate(line):
    if file:
        formatted_map.extend([i // 2 for j in range(int(char))])
        file = False
    else:
        formatted_map.extend(["." for j in range(int(char))])
        file = True


map_length = len(formatted_map)-1
pointer = 0
for i, char in enumerate(reversed(formatted_map)):
    pointer = get_free_pointer(formatted_map, pointer)
    if pointer < map_length-i:
        formatted_map[pointer] = char
        formatted_map[map_length-i] = "."

part_1 = 0
for i, char in enumerate(formatted_map):
    if char != ".":
        part_1 += i*char

print(f"{part_1=}")