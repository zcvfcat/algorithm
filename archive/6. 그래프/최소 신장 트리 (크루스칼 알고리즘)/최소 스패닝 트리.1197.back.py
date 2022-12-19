import sys
import heapq

input = sys.stdin.readline

node_range, edge_range = map(int, input().split())
edges = []
parent = [0] * (node_range + 1)

for i in range(node_range + 1):
    parent[i] = i

for _ in range(node_range):
    node, edge, weight = map(int, input().split())
    heapq.heappush(edges, (weight, node, edge))


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


usedEdge = 0
total = 0

while usedEdge < node_range - 1:
    weight, node, edge = heapq.heappop(edges)

    if find(node) != find(edge):
        union(node, edge)
        total += weight
        usedEdge += 1

print(total)
