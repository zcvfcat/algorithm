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
parents = [node for node in range(node_length + 1)]


def find(a):
    if parents[a] != a:
        parents[a] = find(parents[a])
    return parents[a]


def union(a, b):
    a = find(a)
    b = find(b)

    if b != a:
        parents[b] = a


def kruskal(edges):
    edges = sorted(edges)
    total_cost = 0

    for edge in edges:
        cost, node, near = edge

        if find(node) != find(near):
            union(node, near)
            total_cost += cost

    return total_cost


print(kruskal(edges))
