from collections import deque

node_range, edge_range = map(int, input().split())
graph = [[] for _ in range(node_range + 1)]
in_degree = [0] * (node_range + 1)

for _ in range(edge_range):
    node, edge = map(int, input().split())
    graph[node].append(edge)
    in_degree[edge] += 1


q = deque()

for node in range(1, node_range + 1):
    if in_degree[node] == 0:
        q.append(node)

while q:
    node = q.popleft()

    print(node, end=' ')

    for edge in graph[node]:
        in_degree[edge] -= 1

        if in_degree[edge] == 0:
            q.append(edge)
