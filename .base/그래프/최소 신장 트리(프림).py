import heapq

node_length = 3
edge_length = 3

# [node : [(cost, node, edge)]]
graph = [
    [],
    [(1, 2), (3, 3)],
    [(2, 3), (1, 1)],
    [(3, 1), (2, 2)],
]

visited = [False for _ in range(node_length + 1)]

q = [(0, 1)]

ans = 0
count = 0

while q:
    if count == node_length:
        break

    cost, node = heapq.heappop(q)

    if not visited[node]:
        visited[node] = True
        ans += cost

        for cost, edge in graph[node]:
            heapq.heappush(q, (cost, edge))

print(ans)
