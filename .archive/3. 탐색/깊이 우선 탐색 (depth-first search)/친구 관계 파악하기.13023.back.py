import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m = map(int, input().split(' '))
graph = [[] for _ in range(n)]
visited = [False] * n

isFiveFriend = False

for _ in range(m):
    node, edge = map(int, input().rstrip().split(' '))
    graph[node].append(edge)
    graph[edge].append(node)


def recur_dfs(node, depth):
    if depth == 5:
        print(1)
        exit()

    visited[node] = True
    for edge in graph[node]:
        if not visited[edge]:
            recur_dfs(edge, depth + 1)

    visited[node] = False


for i in range(n):
    recur_dfs(i, 0)

print(0)
