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
    visited[node] = True
    path = [node]

    for edge in graph[node]:
        if visited[edge] is False:
            path += dfs(graph, edge)
    
    return path

path = dfs(graph, 1)
print(path)