visited = []

def dfs(graph, node):
    for edge in graph[node]:
        if visited[edge] is False:
            dfs(graph, edge)