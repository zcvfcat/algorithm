"""
수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.
"""

import sys
from collections import deque
input = sys.stdin.readline

# 첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

n, k = map(int, input().split())
path = [False] * 100_001

step = [lambda x: x + 1, lambda x: x - 1, lambda x: x * 2]


def is_boundary(x):
    return 0 <= x <= 100000


def bfs(start_node):
    global k
    q = deque([(start_node, 0)])
    path[start_node] = start_node

    while q:
        node, count = q.popleft()
        if k == node:
            return count

        for l in step:
            edge = l(node)

            if is_boundary(edge) and not path[edge]:
                path[edge] = node
                q.append((edge, count + 1))


count = bfs(n)

prev = k
paths = [prev]
while prev != n:
    paths.append(path[prev])
    prev = path[prev]

paths.reverse()
print(count)
print(' '.join(map(str, paths)))
