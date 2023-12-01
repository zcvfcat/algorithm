from itertools import permutations


def create_list(s):
    l = []
    k = list(str(s))

    for i in range(0, len(k), 2):
        for _ in range(int(k[i + 1])):
            l.append(k[i])

    return l


def filter_arr(arr):
    k = len(str(arr[0]))
    m = int('1' + '0' * (k - 1))

    return sorted([*filter(lambda t: t >= m, arr)])


def solution(s1, s2):
    s1 = create_list(s1)
    k = permutations(s1, len(s1))
    permuted_s1 = [*map(lambda a: int(''.join(a)), k)]
    s1 = filter_arr(permuted_s1)

    s2 = create_list(s2)
    k = permutations(s2, len(s2))
    permuted_s2 = [*map(lambda a: int(''.join(a)), k)]
    s2 = filter_arr(permuted_s2)

    for v in s2:
        if v + 1 in s1:
            return [v, v + 1]
        if v - 1 in s1:
            return [v - 1, v]


print(solution(2131, 1131))
