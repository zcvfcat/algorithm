from collections import Counter


def solution(n, computers):
    parent = [i for i in range(n)]

    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]

    def union(node_a, node_b):
        node_a = find(node_a)
        node_b = find(node_b)

        if node_a <= node_b:
            parent[node_b] = node_a
        else:
            parent[node_a] = node_b

    for node_index in range(n):
        for edge_index in range(n):

            if node_index == edge_index:
                continue

            if computers[node_index][edge_index] == 1:
                union(node_index, edge_index)

    return len(Counter(parent))


print(solution(3,	[[1, 1, 0], [1, 1, 0], [0, 0, 1]]) == 2)
print(solution(3,	[[1, 1, 0], [1, 1, 1], [0, 1, 1]]) == 1)
