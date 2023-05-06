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

def find(node):
    if parents[node] != node:
        parents[node] = find(parents[node])
    return parents[node]


def union(a, b):
    a = find(a)
    b = find(b)

    if b != a:
        parents[b] = a


def kruskal(edges: list):
    edges.sort()

    cost = 0

    for weight, node, edge in edges:
        if find(node) != find(edge):
            union(node, edge)
            cost += weight
    
    return cost

cost = kruskal(edges)

print(cost)
print(parents)