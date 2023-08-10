node_range = 7
visited = [False] * (node_range + 1)
tree = [
    [],
    [6, 4],
    [4],
    [6, 5],
    [1, 2, 7],
    [3],
    [1, 3],
    [4]
]

ans = [0] * (node_range + 1)


def recur_dfs(node):
    visited[node] = True

    for edge in tree[node]:
        if not visited[edge]:
            ans[edge] = node
            recur_dfs(edge)


recur_dfs(1)

for node in range(2, node_range + 1):
    print(ans[node])
