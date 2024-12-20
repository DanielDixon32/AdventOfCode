import heapq

def print_grid(grid):
    for row in grid:
        print("".join(row))

def dijkstras(grid, start, end):
    rows = len(grid)
    cols = len(grid[0])
    
    pq = [(0, start[0], start[1])]
    
    distances = {(x, y): float('inf') for x in range(rows) for y in range(cols)}
    distances[start] = 0
    
    while pq: 
        dist, x, y = heapq.heappop(pq)

        if (x, y) == end:
            return dist

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != '#':
                new_dist = dist + 1
                if new_dist < distances[(nx, ny)]:
                    distances[(nx, ny)] = new_dist
                    heapq.heappush(pq, (new_dist, nx, ny))
    return -1


with open('input.txt') as file:
    grid = [list(line.strip()) for line in file]

start = None
end = None
walls = set()

for y, row in enumerate(grid):
    for x, val in enumerate(row):
        if val == "S":
            start = (y, x)
        elif val == "E":
            end = (y, x)
        elif val == "#":
            walls.add((y, x))


benchmark = dijkstras(grid, start, end)
total = 0
times = []
for wall in walls:
    y, x = wall

    grid[y][x] = "."
    
    modified_time = dijkstras(grid, start, end)
    if benchmark - modified_time >= 100:
        total += 1
    # times.append(modified_time)
    
    grid[y][x] = "#"

print(total)