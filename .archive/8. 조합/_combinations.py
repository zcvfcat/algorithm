"""
combination([0,1,2,3], 2) = ([0], combination([1, 2, 3], 1)) +
                            ([1], combination([2, 3], 1)) +
                            ([2], combination([3], 1)))
"""


def combinations(array, times):
    if times == 0:
        return [[]]

    ans = []

    for i in range(len(array)):
        element = array[i]

        for rest in combinations(array[i + 1:], times - 1):
            ans.append([element, *rest])

    return ans


print(combinations([0, 1, 2, 3], 2))
