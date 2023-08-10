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

start_node = 1
visited = [False] * (len(graph) + 1)
searched = []


def dfs(node):
    visited[node] = True
    searched.append(node)
    for edge in graph[node]:
        if not visited[edge]:
            dfs(edge)


dfs(start_node)

print(searched)
