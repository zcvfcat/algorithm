graph = [
    [],
    [2, 3, 8],
    [1, 6, 8],
    [1, 4, 5],
    [3],
    [3],
    [2, 7],
    [6],
    [1, 2],
]

visited = [False for _ in range(len(graph))]

def dfs(graph, node):
    for edge in graph[node]:
        if visited[edge] is False:
            visited[edge] = True
            dfs(graph, edge)

dfs(graph, 1)
print(visited)