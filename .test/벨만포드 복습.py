INF = float('inf')

edges = [
    [1, 2, 4],
    [1, 3, 3],
    [2, 3, -1],
    [3, 1, -2],
]

node_length = 3
edge_length = 4
distance = [INF for _ in range(node_length + 1)]

def bellman_ford(start_node):
    distance[start_node] = 0

    for cycle in range(node_length):
        for node, edge, cost in edges:
            edge_cost = distance[node] + cost

            if distance[node] != INF and distance[edge] > edge_cost:
                distance[edge] = edge_cost

                if cycle == node_length - 1:
                    return False

    return True

if bellman_ford(1):
    for node in range(1, node_length + 1):
        if distance[node] == INF:
            print("도달 할 수 없음")
        else:
            print("node: ", node, " cost: ",distance[node])
else:
    print("negative cycle exist")