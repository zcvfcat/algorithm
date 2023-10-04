from math import inf

# O(v^3)
def floyd(graph):
    # 2차 인접 행렬
    distances = [[inf for _ in range(len(graph))] for _ in range(len(graph))]

    for node in range(len(graph)):
        distances[node][node] = 0
    
    # graph 2차 배열
    # (edge, cost)
    for node, edges in enumerate(graph):
        for edge, cost in edges:
            distances[node][edge] = cost
    
    for route in range(len(graph)):
        for node in range(len(graph)):
            for edge in range(len(graph)):
                distances[node][edge] = min(distances[node][edge], distances[node][route] + distances[route][edge])
    
    # 2차 인접 행렬 (node -> edge 최소비용 리턴)
    return distances

