# Part 1
import math

width = 101
height = 103

with open("input.txt") as f:
    robots_text = f.read().split("\n")
    robots = []
    for robot_text in robots_text:
        robot_text = robot_text.split(" ")
        robot_position = list(map(int, robot_text[0][2:].split(",")))
        robot_velocity = list(map(int, robot_text[1][2:].split(",")))
        robots.append([robot_position, robot_velocity])

for robot in robots:
    for i in range(100):
        robot[0][0] = (robot[0][0] + robot[1][0]) % width
        robot[0][1] = (robot[0][1] + robot[1][1]) % height

half_width = (width - 1) // 2
half_height = (height - 1) // 2
quadrants = [0, 0, 0, 0]

for robot in robots:
    robot_position = robot[0]
    if robot_position[0] == half_width or robot_position[1] == half_height:
        ...
    else:
        if robot_position[0] < half_width:
            if robot_position[1] < half_height:
                quadrants[0] += 1
            else:
                quadrants[2] += 1
        else:
            if robot_position[1] > half_height:
                quadrants[3] += 1
            else:
                quadrants[1] += 1

part_1 = math.prod(quadrants)
print(f"{part_1=}")

# Part 2
import math

width = 101
height = 103

with open("input.txt") as f:
    robots_text = f.read().split("\n")
    robots = []
    for robot_text in robots_text:
        robot_text = robot_text.split(" ")
        robot_position = list(map(int, robot_text[0][2:].split(",")))
        robot_velocity = list(map(int, robot_text[1][2:].split(",")))
        robots.append([robot_position, robot_velocity])

i = 0
while i < 10000:
    output = ""
    output += str(i + 1) + "\n"
    for robot in robots:
        robot[0][0] = (robot[0][0] + robot[1][0]) % width
        robot[0][1] = (robot[0][1] + robot[1][1]) % height
    robot_locations = [robot[0] for robot in robots]
    for y in range(height):
        for x in range(width):
            if [x, y] in robot_locations:
                output += "X"
            else:
                output += " "
        output += "\n"
    with open("output.txt", "a") as f:
        f.write(output)
    i += 1