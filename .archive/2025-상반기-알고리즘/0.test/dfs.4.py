def dfs(graph, visited, node, endpoint):
    if node == endpoint:
        return True

    for edge in graph[node]:
        if not visited[edge]:
            visited[edge] = True
            if dfs(graph, visited, edge, endpoint):
                return True

    return False