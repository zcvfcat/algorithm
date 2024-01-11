def binary_search(arr: list[int], target: int):
    arr.sort()  # 오름 차순
    left, right = 0, len(arr)

    while left < right:
        mid = (left + right) // 2
        value = arr[mid]

        if value < target:
            left = mid + 1
        elif value > target:
            right = mid - 1
        else:
            return mid

    return None


def recur_binary_search(arr: list[int], target, left, right):
    if left > right:
        return None

    mid = (left + right) // 2
    value = arr[mid]

    if value < target:
        return recur_binary_search(arr, target, mid + 1, right)
    elif value > target:
        return recur_binary_search(arr, target, left, mid - 1)
    return mid


array = [0, 1, 3, 6, 7, 8, 9]
print(binary_search(array,8))
print(recur_binary_search(sorted(array), 8, 0, len(array)))
