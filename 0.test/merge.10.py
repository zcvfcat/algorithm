def merge(array):
    if len(array) < 2:
        return array

    mid = len(array) // 2
    left = merge(array[:mid])
    right = merge(array[mid:])

    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged