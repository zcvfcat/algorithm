from collections import deque


def bfs(graph, start, end):
    visited = [False for _ in range(len(graph))]

    visited[start] = True
    q = deque([start])

    while q:
        node = q.popleft()

        if node == edge:
            return True

        for edge in graph[node]:
            if not visited[edge]:
                visited[edge] = True
                q.append(edge)

    return False
