# # Inefficient part 1
# import numpy as np

# with open("input.txt") as f:
#     content = f.read()
#     machines = content.split("\n\n")

# machines = [machine.split("\n") for machine in machines]
# total_cost = 0

# for machine in machines:
#     button_description_a = machine[0]
#     button_description_b = machine[1]
#     prize_description = machine[2]
#     vector_description_a = button_description_a[10:].split(", ")
#     vector_description_b = button_description_b[10:].split(", ")
#     vector_a = [int(vector_description_a[0][2:]), int(vector_description_a[1][2:])]
#     vector_b = [int(vector_description_b[0][2:]), int(vector_description_b[1][2:])]
#     prize_location_description = prize_description[7:].split(", ")
#     prize_location = [int(prize_location_description[0][2:]), int(prize_location_description[1][2:])]
    
#     lowest_cost = -1

#     for a_presses in range(0, 100+1):
#         for b_presses in range(0, 100+1):
#             crane_position = [0, 0]
#             crane_position = np.add(crane_position, np.multiply(vector_a, a_presses))
#             crane_position = np.add(crane_position, np.multiply(vector_b, b_presses))
#             if np.array_equal(crane_position, prize_location):
#                 cost = a_presses * 3 + b_presses
#                 if lowest_cost < 0 or cost < lowest_cost:
#                     lowest_cost = int(cost)
    
#     if lowest_cost != -1:
#         total_cost += lowest_cost

# part_1 = int(total_cost)
# print(f"{part_1=}")

# Improved part 1
import numpy as np

with open("input.txt") as f:
    content = f.read()
    machines = content.split("\n\n")

machines = [machine.split("\n") for machine in machines]
total_cost = 0

for i, machine in enumerate(machines):
    button_description_a = machine[0]
    button_description_b = machine[1]
    prize_description = machine[2]
    vector_description_a = button_description_a[10:].split(", ")
    vector_description_b = button_description_b[10:].split(", ")
    x_a = int(vector_description_a[0][2:])
    y_a = int(vector_description_a[1][2:])
    x_b = int(vector_description_b[0][2:])
    y_b = int(vector_description_b[1][2:])
    prize_location_description = prize_description[7:].split(", ")
    x_p = int(prize_location_description[0][2:])
    y_p = int(prize_location_description[1][2:])
    button_vector_matrix = np.array([
        [x_a, x_b],
        [y_a, y_b]
    ])
    prize_vector = np.array([
        [x_p],
        [y_p]
    ])
    button_vector_matrix_inverse = np.linalg.inv(button_vector_matrix)
    solution = np.matmul(button_vector_matrix_inverse, prize_vector)
    a_presses = round(solution[0][0])
    b_presses = round(solution[1][0])
    if np.array_equal(np.multiply(np.array([x_a, y_a]), a_presses) + np.multiply(np.array([x_b, y_b]), b_presses), np.array([x_p, y_p])) and a_presses > 0 and b_presses > 0:
        total_cost += a_presses * 3
        total_cost += b_presses

part_2 = int(total_cost)
print(f"{part_2=}")

# Part 2
import numpy as np

with open("input.txt") as f:
    content = f.read()
    machines = content.split("\n\n")

machines = [machine.split("\n") for machine in machines]
total_cost = 0

for i, machine in enumerate(machines):
    button_description_a = machine[0]
    button_description_b = machine[1]
    prize_description = machine[2]
    vector_description_a = button_description_a[10:].split(", ")
    vector_description_b = button_description_b[10:].split(", ")
    x_a = int(vector_description_a[0][2:])
    y_a = int(vector_description_a[1][2:])
    x_b = int(vector_description_b[0][2:])
    y_b = int(vector_description_b[1][2:])
    prize_location_description = prize_description[7:].split(", ")
    x_p = int(prize_location_description[0][2:]) + 10000000000000
    y_p = int(prize_location_description[1][2:]) + 10000000000000
    button_vector_matrix = np.array([
        [x_a, x_b],
        [y_a, y_b]
    ])
    prize_vector = np.array([
        [x_p],
        [y_p]
    ])
    button_vector_matrix_inverse = np.linalg.inv(button_vector_matrix)
    solution = np.matmul(button_vector_matrix_inverse, prize_vector)
    a_presses = round(solution[0][0])
    b_presses = round(solution[1][0])
    if np.array_equal(np.multiply(np.array([x_a, y_a]), a_presses) + np.multiply(np.array([x_b, y_b]), b_presses), np.array([x_p, y_p])) and a_presses > 0 and b_presses > 0:
        total_cost += a_presses * 3
        total_cost += b_presses

part_2 = int(total_cost)
print(f"{part_2=}")