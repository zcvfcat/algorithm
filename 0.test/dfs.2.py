def dfs(graph, start, end, visited):
    visited[start] = True
    if start == end:
        return True
    for neighbor in graph[start]:
        if not visited[neighbor]:
            if dfs(graph, neighbor, end, visited):
                return True
    return False
