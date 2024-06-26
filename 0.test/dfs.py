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