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


def dfs(graph, start_node):
    node_length = len(graph) - 1
    visited = [False for _ in range(node_length + 1)]

    stack = [(start_node)]
    visited[start_node] = True

    while stack:
        node = stack.pop()
        for edge in graph[node]:
            if visited[edge] is False:
                visited[edge] = True
                stack.append(edge)

    return visited


print(dfs(graph, 1))


node_length = len(graph) - 1
visited = [False for _ in range(node_length + 1)]


def recur_dfs(graph, visited, node):
    for edge in graph[node]:
        if visited[edge] is False:
            visited[edge] = True
            recur_dfs(graph, visited, edge)
    return visited


print(recur_dfs(graph, visited, 1))
