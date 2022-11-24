import heapq

node_length = 3
edge_length = 3

edges = [
    [1, 1, 2],
    [2, 2, 3],
    [3, 1, 3],
]

heapq.heapify(edges)
parent = [0] * (node_length + 1)

for i in range(node_length):
    parent[i] = i


def find(node):
    if node == parent[node]:
        return node
    else:
        parent[node] = find(parent[node])
        return parent[node]


def union(node_a, node_b):
    node_a = find(node_a)
    node_b = find(node_b)

    if node_b != node_a:
        parent[node_b] = node_b


usedEdge = 0
total = 0

while usedEdge < node_length - 1:
    weight, node, edge = heapq.heappop(edges)

    if find(node) != find(edge):
        union(node, edge)
        total += weight
        usedEdge += 1

print(total)
