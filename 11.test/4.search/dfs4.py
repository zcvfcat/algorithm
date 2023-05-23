def dfs(graph, start, end):
    visited = [False for _ in range(len(graph))]
    visited[start] = True
    q = [start]

    while q:
        node = q.pop()

        if node == end:
            return True

        for edge in graph[node]:
            if visited[edge] is False:
                visited[edge] = True
                q.append(edge)
    
    return False
