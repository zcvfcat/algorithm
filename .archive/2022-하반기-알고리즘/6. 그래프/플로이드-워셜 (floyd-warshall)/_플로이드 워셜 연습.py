import sys

edges = [[1, 2, 2],
         [1, 3, 3],
         [1, 4, 1],
         [1, 5, 10],
         [2, 4, 2],
         [3, 4, 1],
         [3, 5, 1],
         [4, 5, 3],
         [3, 5, 10],
         [3, 1, 8],
         [1, 4, 2],
         [5, 1, 7],
         [3, 4, 2],
         [5, 2, 4], ]

node_range = 5
edge_range = len(edges)
distance = [[sys.maxsize for j in range(node_range + 1)] for i in range(node_range + 1)]

# 초기화
for node in range(1, node_range + 1):
    distance[node][node] = 0

# 노드 인접 엣지 업데이트
for node, edge, weight in edges:
    if distance[node][edge] > weight:
        distance[node][edge] = weight

# 플로이드-워셜 수행

for mid_node in range(1, node_range):
    for node in range(1, node_range):
        for edge in range(1, node_range):
            distance[node][edge] = min(distance[node][edge], distance[node][mid_node] + distance[mid_node][edge])

for node in range(1, node_range + 1):
    for edge in range(1, node_range + 1):
        if distance[node][edge] == sys.maxsize:
            print(0, end='\t')
        else:
            print(distance[node][edge], end='\t')
    print()
