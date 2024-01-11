from collections import deque

def bfs(graph, start, end):
    visited = [False for _ in range(len(graph))]

    visited[start] = True
    q = deque([start])

    while q:
        node = q.popleft()

        if start == end:
            return True

        for edge in graph[node]:
            if not visited[edge]:
                visited[edge] = True
                q.append(edge)
    
    return False

# 흐음... dfs 계속 돌겠구먼
def dfs(graph, visited, start, end):
    for edge in graph[start]:
        if not visited[edge]:
            visited[edge] = True
            dfs(graph, visited, start, end)