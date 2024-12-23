from collections import defaultdict

connections = []
with open('input.txt') as file:
    for line in file:
        connections.append(line.strip())

# build adjacency lists
graph = defaultdict(set)
for connection in connections:
    a, b = connection.split('-')
    graph[a].add(b)
    graph[b].add(a)

# detect triangles by finding a-c b-c b-a trios
triangles = set()
for a in graph:
    for b in graph[a]:
        if b > a:
            for c in graph[a].intersection(graph[b]):
                if c > b:
                    # sort alphabetically to ensure no duplicates
                    triangles.add(tuple(sorted([a, b, c])))

filtered_triangles = [triangle for triangle in triangles if any(node.startswith('t') for node in triangle)]

print(f'Num of \"triangle\" connections: {len(filtered_triangles)}')
