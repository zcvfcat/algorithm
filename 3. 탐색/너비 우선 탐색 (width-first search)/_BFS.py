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

start_node = 1
visited = [False] * (len(graph) + 1)
searched = []


def bfs(start_node):
    q = deque([start_node])
    visited[start_node] = True

    while q:
        node = q.popleft()
        searched.append(node)

        for edge in graph[node]:
            if not visited[edge]:
                visited[edge] = True
                q.append(edge)

bfs(start_node)

print(searched)