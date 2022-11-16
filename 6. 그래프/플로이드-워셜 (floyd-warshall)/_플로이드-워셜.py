# 모르겠는데?????
import sys
INF = sys.maxsize

node_range = 4

graph = [
    [0, 2, INF, 4],
    [2, 0, INF, 5],
    [3, INF, 0, INF],
    [INF, 2, 1, 0]
]

distance = [[INF for _ in range(node_range)] for _ in range(node_range)]

for node in range(node_range):
    for edge in range(node_range):
        distance[node][edge] = graph[node][edge]

for k in range(node_range):
    for node in range(node_range):
        for edge in range(node_range):
            cost = distance[node][k] + distance[k][edge]
            if distance[node][edge] > cost:
                distance[node][edge] = cost

print(distance)
