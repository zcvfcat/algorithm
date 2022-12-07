node_length = 10
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


union(1, 4)
print(parent)

union(5, 6)
print(parent)

union(1, 6)
print(parent)
