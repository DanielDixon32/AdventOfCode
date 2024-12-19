from collections import defaultdict

with open('input.txt') as file:
    content = file.read()
    
content = content.split("\n")
for i in range(len(content)):
    content[i] = list(content[i])


def print_grid(grid):
    for row in grid:
        print("".join(row))

antennae_pos = {}
for y, line in enumerate(content):
    for x, char in enumerate(line):
        if char != '.':
            if char in antennae_pos:
                antennae_pos[char].append((x, y))
            else:
                antennae_pos[char] = [(x, y)]

antinode_locations = set()
for k in antennae_pos:
    pos_list = antennae_pos[k]
    for p1 in pos_list:
        for p2 in pos_list:
            new_x, new_y = 0, 0
            dx, dy = 0, 0
            if p1 != p2:
                dx = p2[0] - p1[0]
                dy = p2[1] - p1[1]
                new_x = p2[0]
                new_y = p2[1]
                while 0 <= new_x < len(content[0]) and 0 <= new_y < len(content):
                    if content[new_y][new_x] not in antennae_pos:
                        content[new_y][new_x] = "#"
                    antinode_locations.add((new_x, new_y))
                    
                    new_x += dx
                    new_y += dy
print_grid(content)
print(f"Number of antinodes: {len(antinode_locations)}")