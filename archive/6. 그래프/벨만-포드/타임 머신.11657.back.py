import sys
input = sys.stdin.readline

width, edge_range = map(int, input().split())
graph = []
distance = [sys.maxsize] * (width + 1)

for node in range(edge_range):
    node, edge, weight = map(int, input().split())
    graph.append((node, edge, weight))

distance[1] = 0

for node in range(width - 1):
    for node, edge, weight in graph:
        cost = distance[node] + weight

        if distance[node] != sys.maxsize and distance[edge] > cost:
            distance[edge] = cost

isCycle = False

for node, edge, weight in graph:
    cost = distance[node] + weight

    if distance[node] != sys.maxsize and distance[edge] > cost:
        isCycle = True

if not isCycle:
    for node in range(2, width + 1):
        if distance[node] != sys.maxsize:
            print(distance[node])
        else:
            print(-1)
else:
    print(-1)
