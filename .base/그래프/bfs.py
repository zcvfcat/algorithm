from collections import deque

graph = [
    [],
    [2, 3, 8],
    [1, 6, 8],
    [1, 4, 5],
    [3],
    [3],
    [2, 7],
    [6],
    [1, 2],
]

node_length = 8

visited = [False for _ in range(node_length + 1)]


def bfs(start_node):
    q = deque([start_node])
    visited[start_node] = True

    while q:
        node = q.popleft()
        # print(node)
        for edge in graph[node]:
            if not visited[edge]:
                visited[edge] = True
                q.append(edge)


bfs(1)
