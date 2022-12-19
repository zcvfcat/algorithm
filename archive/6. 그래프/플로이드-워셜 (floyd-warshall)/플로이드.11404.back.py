import sys

node_range = int(input())
edge_range = int(input())

# 초기화
distance = [[sys.maxsize for _ in range(node_range + 1)] for _ in range(node_range + 1)]

# 자기자신 업데이트
for node in range(1, node_range + 1):
    distance[node][node] = 0

# 노드 인접 엣지 업데이트
for i in range(edge_range):
    node, edge, weight = map(int, input().split())
    if distance[node][edge] > weight:
        distance[node][edge] = weight

# 플루이드 워셜 점화식

for mid_node in range(1, node_range + 1):
    for node in range(1, node_range + 1):
        for edge in range(1, node_range + 1):
            distance[node][edge] = min(distance[node][edge], distance[node][mid_node] + distance[mid_node][edge])

for node in range(1, node_range + 1):
    for edge in range(1, node_range + 1):
        if distance[node][edge] == sys.maxsize:
            print(0, end=' ')
        else:
            print(distance[node][edge], end=' ')
    print()
