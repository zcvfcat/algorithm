"""
combination([0,1,2,3], 2) = ([0], combination([1, 2, 3], 1)) +
                            ([1], combination([2, 3], 1)) +
                            ([2], combination([3], 1)))
nCr
"""
import itertools


def combinations(array: list, tie: int) -> list:
    ans = []

    if tie == 0:
        return [ans]

    for i in range(len(array)):
        node = array[i]

        for edges in combinations(array[i + 1:], tie - 1):
            ans.append((node, *edges))

    return ans


print(combinations([0, 1, 2, 3], 2))
print([*itertools.combinations([0, 1, 2, 3], 2)])
