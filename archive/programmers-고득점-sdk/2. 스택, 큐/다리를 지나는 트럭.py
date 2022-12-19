# 모르겠는데?

from collections import deque


def solution(bridge_length, weight, truck_weights):
    time = 0
    q = deque([0 for _ in range(bridge_length)])
    trucks = deque(truck_weights)

    while q:
        time += 1
        q.popleft()

        if not trucks:
            continue

        if sum(q) + trucks[0] <= weight:
            q.append(trucks.popleft())
        else:
            q.append(0)

    return time


print(solution(2,	10,	[7, 4, 5, 6]) == 8)
print(solution(100,	100,	[10]) == 101)
print(solution(100,	100,	[10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 110)
