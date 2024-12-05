# Part 1

with open("input.txt") as f:
    input = [line.strip("\n") for line in f]

def get_letter(x, y):
    if x < 0 or y < 0:
        return None
    if x > len(input[0])-1 or y > len(input)-1:
        return None
    return input[y][x]

def initiate_search(x, y):
    count = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if (dx, dy) != (0, 0):
                found_string = search_string[0]
                next_character = get_letter(x+dx, y+dy)
                if next_character == search_string[len(found_string)]:
                    found_string += next_character
                    if continue_search(x+dx, y+dy, dx, dy, found_string):
                        count += 1
    return count

def continue_search(x, y, dx, dy, found_string):
    if len(found_string) == len(search_string):
        return True
    next_character = get_letter(x+dx, y+dy)
    if next_character == search_string[len(found_string)]:
        found_string += next_character
        if continue_search(x+dx, y+dy, dx, dy, found_string):
            return True

search_string = "XMAS"

part_1 = 0

for y, line in enumerate(input):
    for x, letter in enumerate(line):
        if letter == search_string[0]:
            part_1 += initiate_search(x, y)

print(f"{part_1=}")


# Part 2

with open("input.txt") as f:
    input = [line.strip("\n") for line in f]

def get_letter(x, y):
    if x < 0 or y < 0:
        return None
    if x > len(input[0])-1 or y > len(input)-1:
        return None
    return input[y][x]

def initiate_search(x, y):
    count = 0
    for dx in range(-1, 2, 2):
        for dy in range(-1, 2, 2):
            target_character = search_string[0]
            next_character = get_letter(x+dx, y+dy)
            if next_character == target_character:
                if continue_search(x, y, dx, dy):
                    count += 1
    if count == 2:
        return True
    else:
        return False

def continue_search(x, y, dx, dy):
    target_character = search_string[2]
    next_character = get_letter(x-dx, y-dy)
    if next_character == target_character:
        return True

search_string = "MAS"

part_2 = 0

for y, line in enumerate(input):
    for x, letter in enumerate(line):
        if letter == search_string[len(search_string) // 2]:
            if initiate_search(x, y):
                part_2 += 1

print(f"{part_2=}")