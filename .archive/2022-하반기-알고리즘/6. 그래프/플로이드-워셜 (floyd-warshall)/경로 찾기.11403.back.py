import sys
input = sys.stdin.readline

node_range = int(input())
distance = [[0 for _ in range(node_range)] for _ in range(node_range)]

for i in range(node_range):
    distance[i] = list(map(int, input().split()))

for mid_node in range(node_range):
    for node in range(node_range):
        for edge in range(node_range):
            if distance[node][mid_node] == 1 and distance[mid_node][edge]:
                distance[node][edge] = 1

for node in range(node_range):
    for edge in range(node_range):
        print(distance[node][edge], end=' ')
    print()
