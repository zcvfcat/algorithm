# graph = [[], [3, 4], [3, 4, 5], [1, 5], [1], [2, 6], [3, 5]] 숫자만 가능한 graph
# graph = {1: [3, 4], 2: [3, 4, 5], 3: [1, 5], 4: [1], 5: [2, 6], 6: [3, 5]}
# O(V(탐색시작) + E(간선))


graph = [[], [3, 4], [3, 4, 5], [1, 5], [1], [2, 6], [3, 5]]
visited = [False] * len(graph)


def recur_dfs(graph, node):
    visited[node] = True
    for edge in graph[node]:
        if not visited[edge]:
            recur_dfs(graph, edge)


recur_dfs(graph, 1)

visited = [False] * len(graph)


def stack_dfs(graph, node):
    stack = [node]

    while stack:
        node = stack.pop()
        if not visited[node]:
            edges = graph[node]
            stack.extend(edges)
            visited[node] = True


stack_dfs(graph, 1)
