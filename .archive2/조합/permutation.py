"""
permutation([0,1,2,3], 2) = ([0], permutation([1, 2, 3], 1)) +
                            ([1], permutation([0, 2, 3], 1)) +
                            ([2], permutation([0, 1, 3], 1)) +
                            ([3], permutation([0, 1, 2], 1))
"""
import itertools


def permutations(array, tie):
    ans = []

    if tie ==0:
        return [ans]

    for idx in range(len(array)):
        node = array[idx]

        for edges in permutations(array[:idx] + array[idx + 1:], tie - 1):
            ans.append((node, *edges))

    return ans


print(permutations([0, 1, 2, 3], 2))
print([*itertools.permutations([0, 1, 2, 3], 2)])
