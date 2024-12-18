import heapq

def print_grid(grid):
    for row in grid:
        print("".join(row))

def dijkstras(grid, start, end):
    rows = len(grid)
    cols = len(grid[0])
    
    # cost, x, y
    pq = [(0, start[0], start[1])]
    
    distances = {(x, y,):float('inf') for x in range(rows) for y in range(cols)}
    distances[start] = 0
    
    while pq: 
        # get current cost
        dist, x, y = heapq.heappop(pq)

        # end condition
        if (x, y) == end:
            return dist

        # queue new (valid) directions
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
    corruputed_mem = file.readlines()
corruputed_mem = list([tuple(map(int, line.split(","))) for line in corruputed_mem])

grid = [["." for _ in range(71)] for _ in range(71)]

for i in range(1024):
    x, y, = corruputed_mem[i]
    grid[y][x] = "#"
    
start = (0, 0)
end = (70, 70)

print(dijkstras(grid, start, end))