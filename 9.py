# Part 1

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

# Part 2

with open("input.txt") as f:
    line = f.read().strip()

def get_list_item(list, index):
    if index > len(list)-1 or index < 0:
        return None
    else:
        return list[index]

def get_free_pointer(formatted_map, file_length):
    for i in range(map_length):
        adjusted_index = i + 0
        free_space_length = 0
        while get_list_item(formatted_map, adjusted_index+free_space_length) == ".":
            free_space_length += 1
        if free_space_length >= file_length:
            return adjusted_index
    return None

def get_file_length(index, formatted_map):
    map_length = len(formatted_map)-1
    file_id = formatted_map[map_length-index]
    counter = 0
    while get_list_item(formatted_map, map_length-index) == file_id:
        if get_list_item(formatted_map, map_length-index) is None:
            return None
        index += 1
        counter += 1
    return counter

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
i = 0
checked = set()
while i < len(formatted_map):
    char = formatted_map[map_length-i]
    if char != "." and char not in checked:
        file_length = get_file_length(i, formatted_map)
        pointer = get_free_pointer(formatted_map, file_length)
        if pointer is not None and pointer < map_length-i:
            formatted_map[map_length-i-file_length+1:map_length-i+1] = ["." for i in range(file_length)]
            formatted_map[pointer:pointer+file_length] = [char for i in range(file_length)]
        checked.add(char)
    i += 1

part_2 = 0
for i, char in enumerate(formatted_map):
    if char != ".":
        part_2 += i*int(char)

print(f"{part_2=}")