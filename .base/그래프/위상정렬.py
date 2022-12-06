# O(V + E)
from functools import reduce
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

node_length = len(graph) - 1
edges_length = reduce(lambda acc, curr: acc + len(curr), graph, 0)
degrees = [0 for _ in range(node_length + 1)]

q = deque()

# 연결 차수
for edges in graph:
    for edge in edges:
        degrees[edge] += 1

# 시작점 찾기
for node in range(1, node_length):
    if degrees[node] == 0:
        q.append(node)

while q:
    node = q.popleft()  # O(V)
    # print(node)
    for edge in graph[node]:  # O(E)
        degrees[edge] -= 1

        if degrees[edge] == 0:
            q.append(edge)
