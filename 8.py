# Part 1

with open("input.txt") as f:
    lines = [list(i.strip()) for i in f]

def validate_coords(x, y):
    if x > len(lines[0])-1 or y > len(lines)-1:
        return False
    if x < 0 or y < 0:
        return False
    return True

antenna_coords = {}
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char != ".":
            antenna_coords.setdefault(char, []).append((x, y))

antinodes = set()
for frequency in antenna_coords:
    coords = antenna_coords[frequency]
    for coord_pair_1 in coords:
        for coord_pair_2 in coords:
            vector = (coord_pair_2[0]-coord_pair_1[0], coord_pair_2[1]-coord_pair_1[1])
            if vector != (0, 0):
                x, y = coord_pair_1
                dx, dy = vector
                if validate_coords(x-dx, y-dy):
                    antinodes.add((x-dx, y-dy))

part_1 = len(antinodes)
print(f"{part_1=}")

# Part 2

with open("input.txt") as f:
    lines = [list(i.strip()) for i in f]

def validate_coords(x, y):
    if x > len(lines[0])-1 or y > len(lines)-1:
        return False
    if x < 0 or y < 0:
        return False
    return True

antenna_coords = {}
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char != ".":
            antenna_coords.setdefault(char, []).append((x, y))

antinodes = set()
for frequency in antenna_coords:
    coords = antenna_coords[frequency]
    for coord_pair_1 in coords:
        for coord_pair_2 in coords:
            vector = (coord_pair_2[0]-coord_pair_1[0], coord_pair_2[1]-coord_pair_1[1])
            if vector != (0, 0):
                x, y = coord_pair_1
                dx, dy = vector
                while validate_coords(x, y):
                    antinodes.add((x, y))
                    x = x-dx
                    y = y-dy

part_2 = len(antinodes)
print(f"{part_2=}")