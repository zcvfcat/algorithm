from collections import deque


def solution(N, number):
    q = deque([(0, 0)])
    _min = -1

    while q:
        cursor, count = q.popleft()

        if cursor == number and (_min > count or _min == -1):
            _min = count
        elif count > 8:
            continue
        else:
            for i in range(1, 9):
                if count + i > 8:
                    break

                temp = int(str(N) * i)
                q.append([cursor + temp, count + i])
                q.append([cursor - temp, count + i])
                q.append([cursor * temp, count + i])
                q.append([cursor // temp, count + i])

    return _min


print(solution(5, 12) == 4)
print(solution(5, 55) == 2)
print(solution(5, 555) == 3)
print(solution(5, 5555) == 4)
print(solution(5, 111) == 4)
print(solution(5, 111) == 4)
print(solution(5, 111) == 4)
print(solution(2, 11) == 3)
