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

def bfs(graph, start, end):
    visited = [0 for _ in range(len(graph))]

    q = deque([start])
    visited[start] = 1

    while q:
        node = q.popleft()

        if node == end:
            return visited

        for edge in graph[node]:
            if visited[edge] == 0 or visited[edge] > visited[node] + 1:
                visited[edge] = visited[node] + 1
                q.append(edge)

    return None

print(bfs(graph, 1, 7))