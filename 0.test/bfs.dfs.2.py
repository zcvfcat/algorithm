from collections import deque

def dfs(graph, visited, end, node):
    if node == end:
        return visited[node]

    for edge in graph[node]:
        if visited[edge] == -1:
            visited[edge] += visited[node] + 1
            result = dfs(graph, visited, end, edge)

            if result != None:
                return result

    return None


def bfs(graph, start, end):
    visited = [-1 for _ in range(len(graph))]
    visited[start] = 0

    q=deque([start])

    while q:
        node = q.popleft()

        if node == end:
            return visited[node]

        for edge in graph[node]:
            if visited[edge] != -1:
                visited[edge] = visited[node] + 1
                q.append(edge)
    
    return None