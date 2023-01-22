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


def bfs(graph, start_node):
    node_length = len(graph) - 1
    visited = [False for _ in range(node_length + 1)]

    q = deque([(start_node)])
    visited[start_node] = True

    while q:
        node = q.popleft()

        for edge in graph[node]:
            if visited[edge] is False:
                visited[edge] = True
                q.append(edge)

    return visited


print(bfs(graph, 1))
