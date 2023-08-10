# 케빈 베이컨 거리가 가장 가까운 친구를 구하기
# 1 -> 3 -> 2
# 1 ->      3
# 1 ->      4
# 1 -> 4 -> 5

# 2 -> 3 ->         1
# 2 ->              3
# 2 -> 3 ->         4
# 2 -> 3 -> 4 ->    5

# 1 / 2 1 1 2 = 6
# 2 / 2 1 2 3 = 8
# 3 / 1 1 1 2 = 5
# 4 / 1 2 1 1 = 5
# 5 / 1 2 1 1 = 5

import sys

node_range, edge_range = map(int, input().split())
distance = [[sys.maxsize for _ in range(node_range + 1)] for _ in range(node_range + 1)]

# inited distance
for node in range(1, node_range):
    distance[node][node] = 0

# updated connect-distance
for i in range(edge_range):
    node, edge = map(int, input().split())
    distance[node][edge] = 1
    distance[edge][node] = 1

# floyd-warshall
for mid_node in range(1, node_range + 1):
    for node in range(1, node_range + 1):
        for edge in range(1, node_range + 1):
            distance[node][edge] = min(distance[node][edge], distance[node][mid_node] + distance[mid_node][edge])

ans = -1
min_distance = sys.maxsize

# search min-node == social friend
for node in range(1, node_range + 1):
    acc = sum(distance[node][1:])

    if min_distance > acc:
        min_distance = acc
        ans = node

print(ans)
