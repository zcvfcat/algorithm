import heapq

node_length = 3
edge_length = 3

graph = [
    [],
    [(1, 2), (3, 3)],
    [(2, 3), (1, 1)],
    [(3, 1), (2, 2)],
]


visited = [False for _ in range(node_length + 1)]


def prim(start_node):
    q = [(0, start_node)]
    total_cost = 0

    while q:
        cost, node = heapq.heappop(q)

        if not visited[node]:
            visited[node] = True
            total_cost += cost

            for cost, edge in graph[node]:
                heapq.heappush(q, (cost, edge))

    return total_cost


print(visited)
print(prim(1))
