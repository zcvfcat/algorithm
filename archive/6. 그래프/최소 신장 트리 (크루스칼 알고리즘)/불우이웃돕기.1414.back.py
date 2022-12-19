import sys
import heapq

input = sys.stdin.readline
node_range = int(input())
q = []
total = 0
parent = [0] * (node_range)

for node in range(node_range):
    l = list(input())

    for edge in range(node_range):
        weight = 0

        if 'a' <= l[edge] <= 'z':
            weight = ord(l[edge]) - ord('a') + 1
        elif 'A' <= l[edge] <= 'Z':
            weight = ord(l[edge]) - ord('A') + 27

        total += weight

        if node != edge and weight != 0:
            heapq.heappush(q, (weight, node, edge))

for node in range(node_range):
    parent[node] = node


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


useEdge = 0
result = 0

while q:
    weight, node, edge = heapq.heappop(q)

    if find(node) != find(edge):
        union(node, edge)
        result += weight
        useEdge += 1

if useEdge == node_range - 1:
    print(total - result)
else:
    print(-1)
