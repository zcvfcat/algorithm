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

def recur_dfs(node):
    visited[node] = True

    for edge in graph[node]:
        if visited[edge] is False:
            recur_dfs(edge)
    

recur_dfs(1)

print(visited)
