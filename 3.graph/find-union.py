def find(parents, node):
    if parents[node] != node:
        parents[node] = find(parents, parents[node])
    return parents[node]


def union(parents, node_a, node_b):
    node_a = find(parents, node_a)
    node_b = find(parents, node_b)

    if node_b != node_a:
        parents[node_b] = node_a


parents = [node for node in range(10)]

union(parents, 1, 4)
union(parents, 5, 6)
union(parents, 1, 6)

print(parents)

group = set(map(lambda x: find(parents, x), parents))
print(group)
