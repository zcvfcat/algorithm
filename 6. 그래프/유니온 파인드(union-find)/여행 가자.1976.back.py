n = int(input())
m = int(input())

city = [[0 for j in range(n + 1)] for i in range(n + 1)]
parent = [i + 1 for i in range(n)]


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


for i in range(1, n + 1):
    city[i] = list(map(int, input().split()))
    city[i].insert(0, 0)

route = list(map(int, input().split(' ')))
route.insert(0, 0)
