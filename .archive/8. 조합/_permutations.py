"""
permutation([0,1,2,3], 2) = ([0], permutation([1, 2, 3], 1)) +
                            ([1], permutation([0, 2, 3], 1)) +
                            ([2], permutation([0, 1, 3], 1)) +
                            ([3], permutation([0, 1, 2], 1))
"""


def permutation(array, times):
    if times == 0:
        return [[]]

    ans = []

    for i in range(len(array)):
        element = array[i]

        for rest in permutation(array[: i] + array[i + 1:], times - 1):
            ans.append([element, *rest])

    return ans


print(permutation([0, 1, 2, 3], 2))
