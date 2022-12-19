import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

node_range = int(input())
parent = list(map(int, input().split()))
deleted_node = int(input())

visited = [False] * node_range
tree = [[] for _ in range(node_range)]
total = 0
root_node = 0

for node in range(node_range):
    if parent[node] != -1:
        tree[node].append(parent[node])
        tree[parent[node]].append(node)
    else:
        root_node = node


def recur_dfs(node):
    global total
    visited[node] = True

    is_leaf_node = True
    for edge in tree[node]:
        if not visited[edge] and edge != deleted_node:
            is_leaf_node = False
            recur_dfs(edge)

    if is_leaf_node:
        total += 1


if deleted_node == root_node:
    print(0)
else:
    recur_dfs(root_node)
    print(total)
