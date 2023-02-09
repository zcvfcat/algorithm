def permutations(array, tie):
    ans = []

    if tie == 0:
        return [ans]

    for idx, node in enumerate(array):
        for edges in permutations(array[:idx] + array[idx + 1:], tie - 1):
            ans.append([node] + edges)

    return ans


print(permutations([0, 1, 2, 3], 2))
