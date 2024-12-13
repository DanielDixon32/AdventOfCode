grid = []
with open('input.txt') as file:
    for line in file:
        grid.append(list(map(int, list(line.strip()))))

def in_bounds(i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])

def get_valid_adjacent_coords(i, j):
    if not in_bounds(i, j):
        return
    
    to_visit = []
    directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    for dir in directions:
        new_i, new_j = (i + dir[0], j + dir[1])
        
        if not in_bounds(new_i, new_j):
            continue
        elif grid[new_i][new_j] - grid[i][j] == 1:
            to_visit.append((new_i, new_j))
    return to_visit

def explore(i, j):
    visited_peaks = set()
    score = 0
    q = [(i, j)]
    
    while q:
        i, j = q.pop(0)
        
        if grid[i][j] == 9 and (i, j) not in visited_peaks:
            visited_peaks.add((i, j))
            score += 1
        else:
            q.extend(get_valid_adjacent_coords(i, j))
            
    return score
    
total = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 0:
            total += explore(i, j)

print(total)