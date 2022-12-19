from collections import deque


def solution(numbers, target):
    q = deque([(0, -1)])
    ans = []
    while q:
        node, index = q.popleft()

        if index + 1 == len(numbers):
            ans.append(node)
            continue

        next_index = index + 1

        edge = numbers[next_index]

        q.append((node + edge, next_index))
        q.append((node - edge, next_index))

    return ans.count(target)


print(solution([1, 1, 1, 1, 1], 3) == 5)
print(solution([4, 1, 2, 1], 4) == 2)
