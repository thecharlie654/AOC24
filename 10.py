# Part 1

with open("input.txt") as f:
    lines = [list(map(int, i.strip())) for i in f]

def get_value(x, y):
    if x < 0 or y < 0:
        return None
    if x > len(lines[0])-1 or y > len(lines)-1:
        return None
    return lines[y][x]

def scan_routes(x, y, visited_nines):
    count = 0
    height = get_value(x, y)
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            if abs(dx) != abs(dy):
                adjacent_height = get_value(x+dx, y+dy)
                if height == 8 and adjacent_height == 9:
                    if (x+dx, y+dy) not in visited_nines:
                        visited_nines.add((x+dx, y+dy))
                        count += 1
                elif adjacent_height == height+1:
                    count += scan_routes(x+dx, y+dy, visited_nines)
    return count

part_1 = 0
for y, line in enumerate(lines):
    for x, height in enumerate(line):
        if height == 0:
            visited_nines = set()
            trailhead_score = scan_routes(x, y, visited_nines)
            part_1 += trailhead_score

print(f"{part_1=}")

# Part 2

with open("input.txt") as f:
    lines = [list(map(int, i.strip())) for i in f]

def get_value(x, y):
    if x < 0 or y < 0:
        return None
    if x > len(lines[0])-1 or y > len(lines)-1:
        return None
    return lines[y][x]

def scan_routes(x, y):
    count = 0
    height = get_value(x, y)
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            if abs(dx) != abs(dy):
                adjacent_height = get_value(x+dx, y+dy)
                if height == 8 and adjacent_height == 9:
                    visited_nines.add((x+dx, y+dy))
                    count += 1
                elif adjacent_height == height+1:
                    count += scan_routes(x+dx, y+dy)
    return count

part_2 = 0
for y, line in enumerate(lines):
    for x, height in enumerate(line):
        if height == 0:
            trailhead_score = scan_routes(x, y)
            part_2 += trailhead_score

print(f"{part_2=}")