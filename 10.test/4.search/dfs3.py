
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


visited = [0 for _ in range(len(graph))]

def dfs(graph, node, end):
    for edge in graph[node]:
        if visited[edge] == 0 or visited[edge] > visited[node] + 1:
            visited[edge] = visited[node] + 1
            dfs(graph, edge, end)

    return visited[end]

visited[1] = 1
dfs(graph, 1, 7)

print(visited)