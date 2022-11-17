import sys

start_node = 1
node_range = 3
edge_range = 4
edges = [
    (1, 2, 4),
    (1, 3, 3),
    (2, 3, -1),
    (3, 1, -2),
]

distance = [sys.maxsize] * (node_range + 1)


distance[start_node] = 0

for _ in range(node_range - 1):
    for node, edge, weight in edges:

        cost = distance[node] + weight

        if distance[node] != sys.maxsize and distance[edge] > distance[node] + weight:
            distance[edge] = cost

isCycle = False

for node, edge, weight in edges:

    cost = distance[node] + weight

    if distance[node] != sys.maxsize and distance[edge] > cost:
        isCycle = True

if not isCycle:
    for node in range(2, node_range + 1):
        if distance[node] != sys.maxsize:
            print(distance[node])
        else:
            print(-1)

else:
    print(-1)
