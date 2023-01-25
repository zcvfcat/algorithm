node_length = 10
parent = [node for node in range(node_length)]


def find(node):
    if node != parent[node]:
        parent[node] = find(parent[node])
    return parent[node]


def union(node_a, node_b):
    node_a = find(node_a)
    node_b = find(node_b)

    if node_b != node_a:
        parent[node_b] = node_a


union(1, 4)
union(5, 6)
union(1, 6)

groups = set(map(lambda x: find(x), parent))
print(groups)