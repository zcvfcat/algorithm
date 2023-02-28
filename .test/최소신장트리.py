def find(parents, node):
    if parents[node] != node:
        parents[node] = find(parents,parents[node])
    return parents[node]


def union(parents, node_a, node_b):
    node_a = find(parents, node_a)
    node_b = find(parents, node_b)

    if node_b != node_a:
        parents[node_b] = node_a


edges = [
    [29, 1, 2],
    [75, 1, 6],
    [35, 2, 3],
    [34, 2, 6],
    [7, 3, 4],
    [23, 4, 6],
    [13, 4, 7],
    [53, 5, 6],
    [25, 6, 7],
]

node_length = 7
edge_length = 9

# 0 - 7
parents = [i for i in range(node_length + 1)]


def mst():
    edges.sort()
    total = 0

    for edge in edges:
        cost, node_a, node_b = edge

        if find(parents, node_a) != find(parents, node_b):
            union(parents, node_a, node_b)
            total += cost
    return total

print(parents)
print(mst())