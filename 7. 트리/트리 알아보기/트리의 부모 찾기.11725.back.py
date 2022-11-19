import sys
sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

node_range = int(input())
visited = [False] * (node_range + 1)
tree = [[] for _ in range(node_range + 1)]
ans = [0] * (node_range + 1)

for _ in range(1, node_range):
    node_a, node_b = map(int, input().split())

    tree[node_a].append(node_b)
    tree[node_b].append(node_a)


def recur_dfs(node):
    visited[node] = True

    for edge in tree[node]:
        if not visited[edge]:
            ans[edge] = node
            recur_dfs(edge)


recur_dfs(1)

for i in range(2, node_range + 1):
    print(ans[i])
