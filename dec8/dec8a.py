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
            if p1 != p2:
                dx = p2[0] - p1[0]
                dy = p2[1] - p1[1]
                if 0 <= p2[0] + dx < len(content[0]) and 0 <= p2[1] + dy < len(content):
                    content[p2[1] + dy][p2[0] + dx] = "#"
                    antinode_locations.add((p2[0] + dx, p2[1] + dy))

print_grid(content)
print(f"Number of antinodes: {len(antinode_locations)}")