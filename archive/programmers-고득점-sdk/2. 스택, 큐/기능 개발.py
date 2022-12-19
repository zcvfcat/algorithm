from collections import deque


def solution(progresses, speeds):
    ans = []
    q = deque(progresses)
    s = deque(speeds)

    while q:
        count = 0
        for i in range(len(q)):
            q[i] += s[i]

        while q and q[0] >= 100:
            q.popleft()
            s.popleft()
            count += 1

        if count > 0:
            ans.append(count)

    return ans


print(solution([93, 30, 55], [1, 30, 5]) == [2, 1])
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]) == [1, 3, 2])
