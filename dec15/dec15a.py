def simulate_moves(robot_pos, boxes, walls, moves):
    directions = {
        '<': (0, -1),
        '>': (0, 1),
        '^': (-1, 0),
        'v': (1, 0)
    }

    for move in moves:
        dr, dc = directions[move]
        new_robot_pos = (robot_pos[0] + dr, robot_pos[1] + dc)

        if new_robot_pos in walls:
            continue

        stack = []
        current_pos = new_robot_pos

        while current_pos in boxes:
            stack.append(current_pos)
            current_pos = (current_pos[0] + dr, current_pos[1] + dc)

        if current_pos in walls or current_pos in boxes:
            continue

        for box_pos in reversed(stack):
            boxes.remove(box_pos)
            new_box_pos = (box_pos[0] + dr, box_pos[1] + dc)
            boxes.add(new_box_pos)

        robot_pos = new_robot_pos

    return boxes

def calculate_gps_coordinates(boxes):
    return sum(100 * r + c for r, c in boxes)


with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

split_index = next(i for i, line in enumerate(lines) if not line.startswith("#"))
map_data = lines[:split_index]
move_sequence = "".join(lines[split_index:])

robot_pos = None
boxes = set()
walls = set()

for r, row in enumerate(map_data):
    for c, char in enumerate(row):
        if char == '@':
            robot_pos = (r, c)
        elif char == 'O':
            boxes.add((r, c))
        elif char == '#':
            walls.add((r, c))
            
final_boxes = simulate_moves(robot_pos, boxes, walls, move_sequence)
print("Sum of GPS coordinates:", calculate_gps_coordinates(final_boxes))
