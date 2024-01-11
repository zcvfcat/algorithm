def search(arr, target):
    lo, hi = 0, len(arr)
    arr.sort()

    while lo < hi:
        mid = (lo + hi) // 2

        if target > arr[mid]:
            lo = mid + 1
        elif target < arr[mid]:
            hi = mid - 1
        else:
            return mid

    return None


def recur(arr, target, lo, hi):
    if lo > hi:
        return None

    mid = (lo + hi) // 2

    if target > arr[mid]:
        return recur(arr, target, mid + 1, hi)
    elif target < arr[mid]:
        return recur(arr, target, lo, mid - 1)
    else:
        return mid


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a.sort()

print(recur(a, 5, 0, len(a)))
