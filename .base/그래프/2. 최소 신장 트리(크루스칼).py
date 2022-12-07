import heapq

node_length = 3
edge_length = 3

# cost, node, edge
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


total_cost = 0

while edges:
    cost, node, edge = heapq.heappop(edges)

    start_node = find(node)
    start_edge = find(edge)

    if start_node != start_edge:
        union(start_node, start_edge)
        total_cost += cost

print(total_cost)
