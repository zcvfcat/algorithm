from math import inf
from collections import deque

graph = [
    [],
    [2, 5],
    [3, 6],
    [4],
    [7],
    [6],
    [4],
    [],
]

node_length = len(graph)
degrees = [0 for _ in range(node_length)]
q = deque([])

for edges in graph:
    for edge in edges:
        degrees[edge] += 1

for i in degrees:
    if i == 0:
        q.append(i)

while q:
    node = q.popleft()

    for edge in graph[node]:
        degrees[edge] -= 1

        if degrees[edge] == 0:
            q.append(edge)