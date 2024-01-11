def dfs(graph, node, visited):
    for edge in graph[node]:
        if visited[edge] is False:
            visited[edge] = True
            dfs(graph, edge, visited)
    