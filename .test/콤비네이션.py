def combination(array, tie):
    ans = []

    if tie == 0:
        return [ans]

    for idx in range(len(array)):
        node = array[idx]

        for edges in combination(array[idx + 1:], tie - 1): ### combination 후 iterator로 나옴
            ans += [(node, *edges)]

    return ans


print(combination([0, 1, 2, 3], 2))
