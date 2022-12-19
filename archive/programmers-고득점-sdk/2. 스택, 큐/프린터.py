# from collections import deque


# def solution(priorities, location):
#     ans = 0
#     q = deque([(priority, index) for index, priority in enumerate(priorities)])

#     while q:
#         priority, index = q.popleft()

#         if any(priority < p for p, i in q):
#             q.append((priority, index))

#         else:
#             ans += 1
#             if index == location:
#                 break
#     return ans

# from collections import deque


def solution(priorities, location):
    jobs = len(priorities)
    ans = 0
    cursor = 0

    while True:
        if max(priorities) == priorities[cursor % jobs]:
            priorities[cursor % jobs] = 0
            ans += 1

            if cursor % jobs == location:
                break
        cursor += 1

    return ans


print(solution([2, 1, 3, 2], 2) == 1)
print(solution([1, 1, 9, 1, 1, 1], 0) == 5)
