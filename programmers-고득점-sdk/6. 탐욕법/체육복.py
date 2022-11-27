def solution(n, lost, reserve):
    person = [1 for _ in range(n + 1)]

    for i in lost:
        person[i] -= 1

    for i in reserve:
        person[i] += 1

    for i in range(n):
        if person[i] == 2 and person[i - 1] == 0:
            person[i - 1] += 1
            person[i] -= 1
        elif person[i] == 2 and person[i + 1] == 0:
            person[i + 1] += 1
            person[i] -= 1

    return len(list(filter(lambda x: x >= 1, person))) - 1


print(solution(5, [2, 4], [1, 3, 5]) == 5)
print(solution(5, [2, 4], [3]) == 4)
print(solution(3, [3], [1]) == 2)
