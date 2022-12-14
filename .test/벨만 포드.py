import sys
INF = sys.maxsize

node_length = 3
edge_length = 4

# node edge cost
edges = [
    [1, 2, 4],
    [1, 3, 3],
    [2, 3, -1],
    [3, 1, -2],
]
start_node = 1
distance = [INF for _ in range(node_length + 1)]


def bellman_ford(edges, start_node):
    distance[start_node] = 0

    for cycle in range(node_length):
        for node, edge, cost in edges:
            edge_cost = distance[node] + cost

            if distance[node] != INF and distance[edge] > edge_cost:
                distance[edge] = edge_cost

                if cycle == node_length - 1:  # 끝까지 갱신이 될꺼니까
                    return False

    return True

isCycle = bellman_ford(edges, 1)

if isCycle:
    for node in range(2, node_length + 1): # start_node = 1 이니까 2부터 시작
        if distance[node] == INF:
            print('도달 할 수 없다')
        else:
            print(distance[node])
else:
    print('negative')