from math import inf
from heapq import heappush, heappop

# from collections import deque
# def dijkstra(graph, start_node):
#     distance = [inf for _ in range(len(graph))]
#     distance[start_node] = 0

#     q = deque([(start_node, 0)])

#     while q:
#         node, pre_sum_cost = q.popleft()

#         if distance[node] < pre_sum_cost:
#             continue

#         for edge, cost in graph[node]:
#             next_cost = pre_sum_cost + cost

#             if distance[edge] > next_cost:
#                 distance[edge] = next_cost
#                 q.append((edge, next_cost))

#     return distance


def dijkstra(graph, start_node):
    distance = [inf for _ in range(len(graph))]
    distance[start_node] = 0

    q = []
    heappush(q, (distance[start_node], start_node))

    while q:
        pre_sum_cost, node = heappop(q)

        if distance[node] < pre_sum_cost:
            continue

        for edge, cost in graph[node]:
            next_cost = pre_sum_cost + cost

            if distance[edge] > next_cost:
                distance[edge] = next_cost
                heappush(q, (next_cost, edge))

    return distance


# (edge, cost)
graph = [
    [],
    [(2, 1), (3, 3)],
    [(3, 1), (4, 5)],
    [(4, 2)],
    [],
    [(1, 1)]
]

distance = dijkstra(graph, 1)

print(distance)
