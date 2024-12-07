# up->right, right->down, down->left, left->up
direction_changes = {
    (-1,0):(0,1),
    (0,1):(1,0),
    (1,0):(0, -1),
    (0, -1):(-1,0)
}

grid = []
with open('input.txt') as file:
    for line in file:
        line = line.strip()
        line_content = []
        for char in line:
            line_content.append(char)
        grid.append(line_content)

initial_position = [0, 0]
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "^":
            initial_position = [i, j]
            break

visited = set()
curr_position = initial_position
curr_direction = [-1, 0]

while 0 <= curr_position[0] < len(grid) and 0 <= curr_position[1] < len(grid[i]) and len(visited) < len(grid) * len(grid[0]):
    visited.add(tuple(curr_position))
    
    new_i = curr_position[0] + curr_direction[0]
    new_j = curr_position[1] + curr_direction[1]
    
    if not (0 <= new_i < len(grid) and 0 <= new_j < len(grid[i])):
        break
    
    if str(grid[new_i][new_j]) == "#":
        curr_direction = direction_changes[tuple(curr_direction)]
        
    curr_position[0] += curr_direction[0]
    curr_position[1] += curr_direction[1]
    
    
print(len(visited))