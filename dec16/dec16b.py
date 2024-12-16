import heapq
import copy
  
DIRS = [
    (0, 1),  # Right
    (1, 0),  # Down
    (0, -1), # Left
    (-1, 0)  # Up
]

def in_bounds(pos, board):
    return 0 <= pos[0] < len(board) and 0 <= pos[1] < len(board[pos[0]])
    
def get_neighbors(pos, direction, board):
    r, c = pos[0], pos[1]
    dr, dc = DIRS[direction]
    new_r, new_c = r + dr, c + dc
    
    neighbors = []
    # get marginal cost for current direction:
    if in_bounds((new_r, new_c), board) and board[new_r][new_c] != '#':
        neighbors.append(((new_r, new_c), direction, 1)) # cost of 1 for moving in the same direction

    # get marginal cost for rotaions:
    for turn in [-1, 1]:
        new_direction = (direction + turn) % 4
        neighbors.append(((r, c), new_direction, 1000))
    
    return neighbors

def find_lowest_score_paths(board, start, end):
    # (score, position, direction)
    pq = [(0, start, 0, [start])]
    visited = set()
    
    # dijkstra's algorithm
    while pq:
        # get current cheapest move
        curr_score, curr_pos, curr_dir, curr_path = heapq.heappop(pq)
            
        if curr_pos in visited:
            continue
        visited.add((curr_pos, curr_dir))
        curr_path.append(curr_pos)
        
        # If we have found the end, pop all the paths with the minimum
        if curr_pos == end:
            min_score = curr_score
            paths = []
            
            while min_score == curr_score and len(pq) != 0:
                paths.append(curr_path)
                curr_score, _, _, curr_path = heapq.heappop(pq)
            
            return paths
        
        for neighbor_pos, neighbor_dir, marginal_cost in get_neighbors(curr_pos, curr_dir, board):
            if (neighbor_pos, neighbor_dir) not in visited:
                heapq.heappush(pq, (curr_score + marginal_cost, neighbor_pos, neighbor_dir, copy.copy(curr_path)))
    return float('inf')

with open('input.txt') as file:
    input_str = file.read()
    
board = []
start, end = None, None
for r, row in enumerate(input_str.splitlines()):
    row_list = list(row)
    for c, val in enumerate(row):
        if val == 'S':
            start = (r, c)
        elif val == 'E':
            end = (r, c)
    board.append(row_list)
    
 
seats = set()
minimum_paths = find_lowest_score_paths(board, start, end)
seats = set([curr for row in minimum_paths for curr in row]) # i love list comprehensions
print(f'Seats: {len(seats)}')