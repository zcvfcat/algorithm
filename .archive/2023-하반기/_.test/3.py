from itertools import permutations


def changed(s: int):
    l = str(s)
    merged = []

    for i in range(0, len(l), 2):
        for _ in range(int(l[i + 1])):
            merged.append(l[i])

    permuted = permutations(merged, len(merged))

    k = 10**(len(merged)-1)

    l = [*map(lambda a: int(''.join(a)), set(permuted))]
    b = sorted([*filter(lambda a: a >= k, l)])

    return b


def solution(s1: int, s2: int):
    p1, p2 = changed(s1), changed(s2)

    for v1 in p1:
        if v1 - 1 in p2:
            return [v1 - 1, v1]
        if v1 + 1 in p2:
            return [v1, v1 + 1]



print(solution(1103, 1202))
