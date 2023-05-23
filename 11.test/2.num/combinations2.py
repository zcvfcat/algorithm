def combi(arr, tie):
    if tie == 0:
        return [[]]

    ans = []

    for index, value in enumerate(arr):
        for edges in combi(arr[index:], tie - 1):
            ans.append([value, *edges])

    return ans

