def merge(arr, left, mid, right):
    temp = []
    i, j = left, mid
    while i < mid and j < right:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1
    while i < mid:
        temp.append(arr[i])
        i += 1
    while j < right:
        temp.append(arr[j])
        j += 1
    # 원본 배열에 병합 결과 복사
    for k in range(len(temp)):
        arr[left + k] = temp[k]


def merge_sort_bottom_up(arr):
    n = len(arr)
    size = 1
    while size < n:
        for left in range(0, n, size * 2):
            mid = min(left + size, n)
            right = min(left + size * 2, n)
            merge(arr, left, mid, right)
        size *= 2
    return arr
