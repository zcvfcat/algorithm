import sys
sys.setrecursionlimit(10000)

node_range = 6
parent = [node for node in range(node_range+1)]


def find(node):
    if node == parent[node]:
        return node
    else:
        parent[node] = find(parent[node])
        return parent[node]


def union(node_a, node_b):
    parent_node_a = find(node_a)
    parent_node_b = find(node_b)

    if parent_node_b != parent_node_a:
        parent[parent_node_b] = parent_node_a


union(1, 4)
print(parent[1:])

union(5, 6)
print(parent[1:])

union(1, 6)
print(parent[1:])
