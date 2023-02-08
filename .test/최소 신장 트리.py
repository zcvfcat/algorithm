def find(parents: list, node):
    if node != parents[node]:
        parents[node] = find(parents, parents[node])
    return parents[node]


def union(parents, node_y, node_x):
    group_y = find(parents, node_y)
    group_x = find(parents, node_x)

    if group_y != group_x:
        parents[group_y] = group_x


def kruskal(edges):
    sorted_edges = sorted(edges)
    total_cost = 0

    for edge in sorted_edges:
        cost, node_y, node_x = edge

        if find(parents, node_y) != find(parents, node_x):
            union(parents, node_y, node_x)
            total_cost += cost

    return total_cost


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

parents = [node for node in range(node_length + 1)]

print(parents)
print(kruskal(edges))
