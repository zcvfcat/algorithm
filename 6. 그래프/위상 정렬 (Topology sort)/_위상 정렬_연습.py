from collections import deque

node_range = 7
edge_range = 8
degrees = [0] * (node_range + 1)
ans = []

graph = [
    [],
    [2, 5],
    [3, 6],
    [4],
    [7],
    [6],
    [4],
    [],
]

for edges in graph:
    for edge in edges:
        degrees[edge] += 1

q = deque()

# 시작값 저장
for node in range(1, node_range):
    if degrees[node] == 0:
        q.append(node)


# 연결 차수 끊기
while q:
    node = q.popleft()
    ans.append(node)

    for edge in graph[node]:
        degrees[edge] -= 1

        if degrees[edge] != 0:
            continue

        q.append(edge)

print(ans)
