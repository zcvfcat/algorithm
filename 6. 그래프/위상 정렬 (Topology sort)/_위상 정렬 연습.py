from collections import deque

node_range = 7
edge_range = 8
in_degree = [0] * (node_range + 1)
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

# 노드의 차수 설정
for edges in graph:
    for edge in edges:
        in_degree[edge] += 1

q = deque()

# 시작값 찾기
for node in range(1, node_range):
    if in_degree[node] == 0:
        q.append(node)

while q:
    node = q.popleft()
    ans.append(node)  # 노드 순서대로 넣기

    for edge in graph[node]:  # 노드와 연결된 엣지 서치
        in_degree[edge] -= 1  # 연결된 엣지 1 차수 제거

        if in_degree[edge] == 0:  # 연결된 엣지가 더 이상 없는지
            q.append(edge)  # Queue에 엣지 넣기

print(ans)
