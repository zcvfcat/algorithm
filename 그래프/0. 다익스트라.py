# O(E logV)
import heapq

INF = float('inf')

# edge weight
graph = [
    [],
    [(2, 1), (3, 3)],
    [(3, 1), (4, 5)],
    [(4, 2)],
    [],
    [(1, 1)]
]

node_length = len(graph) - 1
start_node = 1
distance = [INF for _ in range(node_length + 1)]
visited = [False for _ in range(node_length + 1)]

def dijkstra(start_node):
    distance[start_node] = 0

    q = []
    heapq.heappush(q,(start_node, 0 ))

    while q:
        node, passed_weight = heapq.heappop(q)

        if distance[node] > passed_weight:
            continue

        for edge, weight in graph[node]:
            cost = passed_weight + weight

            if distance[edge] > cost:
                distance[edge] = cost

                heapq.heappush(q,(edge, cost))

    return distance

print(dijkstra(1))