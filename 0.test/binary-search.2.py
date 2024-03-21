def binary(arr, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2
    v = arr[mid]

    if v < target:
        return binary(arr, target, start, mid - 1)
    elif v > target:
        return binary(arr, target, mid + 1, end)
    else:
        return mid


def bi(arr, target):
    start, end = 0, len(arr)
    arr.sort()

    while start <= end:
        mid = (start+end)//2
        v = arr[mid]

        if v < target:
            end = mid - 1
        elif v > target:
            start = mid + 1
        else:
            return mid
    return None
