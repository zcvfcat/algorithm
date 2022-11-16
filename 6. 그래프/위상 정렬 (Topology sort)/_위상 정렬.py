from collections import deque

node_range = 7
edge_range = 8
in_degree = [0] * (node_range + 1)
ans = []

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

for edges in graph:
    for edge in edges:
        in_degree[edge] += 1


def topology_sort():
    q = deque()

    for node in range(1, node_range):
        if in_degree[node] == 0:
            q.append(node)

    while q:
        node = q.popleft()
        ans.append(node)

        for edge in graph[node]:
            in_degree[edge] -= 1

            if in_degree[edge] == 0:
                q.append(edge)


topology_sort()
print(ans)
