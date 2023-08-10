visited = []

def dfs(graph, node):
    for edge in graph[node]:
        if visited[edge] is False:
            visited[edge] = True
            dfs(graph, edge)