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

parent = [node for node in range(node_length + 1)]


def find(node):
    if node != parent[node]:
        parent[node] = find(parent[node])
    return parent[node]


def union(node_a, node_b):
    node_a = find(node_a)
    node_b = find(node_b)

    if node_b > node_a:
        parent[node_b] = node_a
    else:
        parent[node_a] = node_b


def kruskal(edges):
    sorted_edges = sorted(edges)  # O(E logE)
    total_cost = 0

    for edge in sorted_edges:
        cost, node_a, node_b = edge

        if find(node_a) != find(node_b):
            union(node_a, node_b)
            total_cost += cost

    return total_cost


print(parent)
print(kruskal(edges))
