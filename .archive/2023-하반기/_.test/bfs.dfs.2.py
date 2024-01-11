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

    return -1


graph = {}
visited = [-1 for _ in range(len(graph))]


def dfs(graph, node, end):
    if node == end:
        return visited[end]

    for edge in graph[node]:
        if visited[edge] == -1:
            visited[edge] = visited[node] + 1
            isEnd = dfs(graph, edge, end)
            if isEnd != -1:
                return isEnd

    return -1
