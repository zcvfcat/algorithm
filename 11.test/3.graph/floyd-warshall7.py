from math import inf

def floyd_warshall(graph):
    distances = [[inf for _ in range(len(graph))] for _ in range(len(graph))]
    
    for node in range(len(distances)):
        distances[node][node] = 0
    
    for node in range(graph):
        for edge, cost in graph[node]:
            distances[node][edge] = cost
    
    length = len(graph)

    for route in range(length):
        for node in range(length):
            for edge in range(length):
                distances[node][edge] = min(distances[node][edge], distances[node][route] + distances[route][edge])
    
    return distances

# 데이터 양식 배열 index node번호, 2차 배열 edge, 비용
graph = [[(1,4)],[(2,4)],[(0,3),(3,1)],[(0,3)]]
