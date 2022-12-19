import sys
sys.setrecursionlimit(10000)

edges = [
    [0, 1, 3],
    [1, 1, 7],
    [0, 7, 6],
    [1, 7, 1],
    [0, 3, 7],
    [0, 4, 2],
    [0, 1, 1],
    [1, 1, 1],
]
node_range = 7
edge_range = 8
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

    if parent_node_a != parent_node_b:
        parent[parent_node_b] = parent_node_a


def isSameParent(node_a, node_b):
    parent_node_a = find(node_a)
    parent_node_b = find(node_b)

    if parent_node_a == parent_node_b:
        return True
    else:
        return False


for question, node_a, node_b in edges:

    if question == 0:
        union(node_a, node_b)
    else:
        if isSameParent(node_a, node_b):
            print('YES')
        else:
            print('NO')
