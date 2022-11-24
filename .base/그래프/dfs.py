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

node_length = 8

visited = [False for _ in range(node_length + 1)]


def recur_dfs(node):
    visited[node] = True
    # print(node)
    for edge in graph[node]:
        if not visited[edge]:
            recur_dfs(edge)


def dfs(start_node):
    stack = [start_node]
    visited[start_node] = True

    while stack:
        node = stack.pop()
        # print(node)
        for edge in graph[node]:
            if not visited[edge]:
                visited[edge] = True
                stack.append(edge)


# recur_dfs(1)
# dfs(1)
