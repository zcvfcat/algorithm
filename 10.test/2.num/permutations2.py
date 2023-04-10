def permutations(arr, tie):
    if tie == 0:
        return [[]]

    ans = []

    for node, value in enumerate(arr):
        for edges in permutations(arr[:node] + arr[node + 1:], tie - 1):
            ans.append([value, *edges])

    return ans
