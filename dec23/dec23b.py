from collections import defaultdict

def bron_kerbosch(R, P, X, graph, cliques):
    if not P and not X:
        cliques.append(R)
        return
    pivot = next(iter(P | X))
    for v in P - graph[pivot]:
        bron_kerbosch(R | {v}, P & graph[v], X & graph[v], graph, cliques)
        P.remove(v)
        X.add(v)


connections = []
with open('input.txt') as file:
    for line in file:
        connections.append(line.strip())

graph = defaultdict(set)
for connection in connections:
    a, b = connection.split('-')
    graph[a].add(b)
    graph[b].add(a)

# find all maximal cliques
cliques = []
bron_kerbosch(set(), set(graph.keys()), set(), graph, cliques)

# find the largest clique
largest_clique = max(cliques, key=len)
password = ','.join(sorted(largest_clique))
print(f"The password is: {password}")
