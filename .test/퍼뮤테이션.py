def permutation(array, tie):
    ans = []

    if tie == 0:
        return [ans]

    for idx in range(len(array)):
        node = array[idx]

        for edges in permutation(array[: idx] + array[idx + 1:], tie - 1):
            ans += [(node, *edges)]

    return ans


print(permutation([0, 1, 2, 3], 2))
