def prefix(array):
    prefix = [0 for _ in range(len(array) + 1)]

    for idx, value in enumerate(array):
        prefix[idx + 1] = prefix[idx] + value

    return prefix


print(prefix([1, 2, 3, 4, 5]))
