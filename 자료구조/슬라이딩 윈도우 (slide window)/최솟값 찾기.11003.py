from collections import deque

n, l = map(int, input().split(' '))
q = deque()
now = list(map(int, input().split(' ')))

for i in range(n):
    while q and q[-1][0] > now[i]:
        q.pop()

    q.append((now[i], i))

    if q[0][1] <= i - l:
        q.popleft()

    print(q[0][0], end=' ')
