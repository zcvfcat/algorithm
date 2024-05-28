from collections import deque


def bfs(graph, start, end):
    visited = [-1 for _ in range(len(graph))]
    visited[start] = 0

    q = deque([start])

    while q:
        node = q.popleft()

        if node == end:
            return visited[end]

        for edge in graph[node]:
            if visited[edge] == -1:
                visited[edge] = visited[node] + 1
                q.append(edge)

    return None


def dfs(graph: list[int], visited: list[int], node: int, end: int):
    if node == end:
        return visited[end]

    for edge in graph[node]:
        if visited[edge] == -1:
            visited[edge] = visited[node] + 1
            result = dfs(graph, visited, edge, end)
            if result != None:
                return result

    return None
