import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write

node_range = int(input())
tree = [[] for _ in range(node_range + 1)]

for _ in range(0, node_range - 1):
    node, edge = map(int, input().split())
    tree[node].append(edge)
    tree[edge].append(node)

depth = [0] * (node_range + 1)
parent = [0] * (node_range + 1)
visited = [False] * (node_range + 1)


def bfs(node):
    queue = deque()
    queue.append(node)

    level = 1
    now_size = 1
    count = 0

    while queue:
        node = queue.popleft()
        visited[node] = True

        for edge in tree[node]:
            if not visited[edge]:
                queue.append(edge)
                parent[edge] = node
                depth[edge] = level

        count += 1

        if count == now_size:
            count = 0
            now_size = len(queue)
            level += 1


bfs(1)


def excute_LCA(node_a, node_b):
    if depth[node_a] < depth[node_b]:
        node_a, node_b = (node_b, node_a)

    while depth[node_a] != depth[node_b]:
        node_a = parent[node_a]

    while node_a != node_b:
        node_a = parent[node_a]
        node_b = parent[node_b]

    return node_a


query = int(input())

for _ in range(query):
    node_a, node_b = map(int, input().split())
    print(str(excute_LCA(node_a, node_b)))
    print('\n')
