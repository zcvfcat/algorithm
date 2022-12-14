graph = {
    1: (2, 3, 8),
    2: (1, 6, 8),
    3: (1, 4, 5),
    4: (3,),
    5: (3,),
    6: (2, 7),
    7: (6,),
    8: (1, 2),
}

node_length = len(graph.keys())

visited = {}
for key in graph.keys():
    visited[key] = False


def recur_dfs(node):
    visited[node] = True

    searched = []
    searched.append(node)

    for edge in graph[node]:
        if not visited[edge]:
            searched.extend(recur_dfs(edge))

    return searched


def dfs(start_node):
    stack = [start_node]
    visited[start_node] = True
    searched = []

    while stack:
        node = stack.pop()
        searched.append(node)

        for edge in graph[node]:
            if not visited[edge]:
                visited[edge] = True
                stack.append(edge)

    return searched


print(recur_dfs(1))
# print(dfs(1))
