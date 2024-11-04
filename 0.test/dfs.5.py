def dfs(graph: list[list[int]], visited: list[int], node: int, end: int):
    if node == end:
        return True
    
    visited[node] = True

    for edge in graph[node]:
        if visited[edge] != -1:
            continue
        visited[edge] = True
        result = dfs(graph, visited, edge, end)
        if result == True:
            return True

    return False
