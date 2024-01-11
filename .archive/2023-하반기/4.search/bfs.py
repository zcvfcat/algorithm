from collections import deque


def bfs(graph: list, start: int):
    visited = [0 for _ in range(len(graph))]
    q = deque([start])

    while q:
        node = q.popleft()

        for edge in graph[node]:
            if visited[edge] is False:
                visited[edge] = True
                q.append(edge)
        
