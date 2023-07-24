from collections import deque


def bfs(graph, start_node):
    visited = [False for _ in range(len(graph))]
    visited[start_node] = True

    q = deque([start_node])

    while q:
        node = q.popleft()

        for edge in graph[node]:
            if visited[edge] is False:
                visited[edge] = True
                q += [edge]

    return visited