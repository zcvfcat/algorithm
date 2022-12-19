from collections import defaultdict
from sys import maxsize


def dfs(node, graph, visited, linked):
    count = 1
    visited[node] = True

    for edge in graph[node]:
        if not visited[edge] and linked[node][edge]:
            count += dfs(edge, graph, visited, linked)

    return count


def solution(n, wires):
    ans = maxsize
    graph = [[] for _ in range(n + 1)]
    linked = [[True] * (n + 1) for _ in range(n + 1)]

    for node, edge in wires:
        graph[node].append(edge)
        graph[edge].append(node)

    for node, edge in wires:
        visited = [False] * (n + 1)

        linked[node][edge] = False
        count_node = dfs(node, graph, visited, linked)
        count_edge = dfs(edge, graph, visited, linked)
        linked[node][edge] = True

        ans = min(ans, abs(count_node - count_edge))

    return ans


# def find(parent, node):
#     if node == parent[node]:
#         return node
#     else:
#         parent[node] = find(parent, parent[node])
#         return parent[node]


# def union(parent, node_a, node_b):
#     node_a = find(parent, node_a)
#     node_b = find(parent, node_b)

#     if node_b != node_a:
#         parent[node_b] = node_a


# def solution(n, wires):
#     ans = maxsize

#     for skip in range(len(wires)):
#         parent = [i for i in range(n + 1)]

#         for idx, wire in enumerate(wires):
#             if skip == idx:
#                 continue
#             if find(parent, wire[0]) != find(parent, wire[1]):
#                 union(parent, wire[0], wire[1])

#         group = defaultdict(int)

#         for i in range(1, n + 1):
#             group[find(parent, i)] + 1

#         group_a, group_b = list(group.values())

#         ans = min(ans, abs(group_a - group_b))

#     return ans


print(solution(9,	[[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]) == 3)
print(solution(4,	[[1, 2], [2, 3], [3, 4]]) == 0)
print(solution(7,	[[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]) == 1)
