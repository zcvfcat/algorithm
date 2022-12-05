"""
이 지렁이는 배추근처에 서식하며 해충을 잡아 먹음으로써 배추를 보호한다. 특히, 어떤 배추에 배추흰지렁이가 한 마리라도 살고 있으면 이 지렁이는 인접한 다른 배추로 이동할 수 있어, 그 배추들 역시 해충으로부터 보호받을 수 있다. 한 배추의 상하좌우 네 방향에 다른 배추가 위치한 경우에 서로 인접해있는 것이다.

한나가 배추를 재배하는 땅은 고르지 못해서 배추를 군데군데 심어 놓았다. 배추들이 모여있는 곳에는 배추흰지렁이가 한 마리만 있으면 되므로 서로 인접해있는 배추들이 몇 군데에 퍼져있는지 조사하면 총 몇 마리의 지렁이가 필요한지 알 수 있다. 예를 들어 배추밭이 아래와 같이 구성되어 있으면 최소 5마리의 배추흰지렁이가 필요하다. 0은 배추가 심어져 있지 않은 땅이고, 1은 배추가 심어져 있는 땅을 나타낸다.

1	1	0	0	0	0	0	0	0	0
0	1	0	0	0	0	0	0	0	0
0	0	0	0	1	0	0	0	0	0
0	0	0	0	1	0	0	0	0	0
0	0	1	1	0	0	0	1	1	1
0	0	0	0	1	0	0	1	1	1
"""

import sys
from collections import deque
input = sys.stdin.readline

step = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def in_boundary(y, x):
    global width, height

    return 0 <= y < height and 0 <= x < width


height = 0
width = 0

testcase = int(input())


def bfs(graph, start_y, start_x):
    q = deque([(start_y, start_x)])
    graph[start_y][start_x] = 0

    while q:
        y, x = q.popleft()

        for dy, dx in step:
            ny = y + dy
            nx = x + dx

            if in_boundary(ny, nx) and graph[ny][nx] == 1:
                graph[ny][nx] = 0
                q.append((ny, nx))


for _ in range(testcase):
    width, height, edge_length = map(int, input().split())
    graph = [[0 for _ in range(width)] for _ in range(height)]
    count = 0

    for _ in range(edge_length):
        x, y = map(int, input().split())
        graph[y][x] = 1

    for y in range(height):
        for x in range(width):
            if graph[y][x] == 1:
                bfs(graph, y, x)
                count += 1

    print(count)
