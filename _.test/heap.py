def heap(arr):
    n = len(arr)

    for i in range(n // 2 - 1, - 1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    return arr


def heapify(arr, n, idx):
    l = idx
    left = 2 * idx + 1
    right = 2 * idx + 2

    # 왼쪽 Node
    if left < n and arr[left] > arr[l]:
        l = left

    # 오른쪽 Node
    if right < n and arr[right] > arr[l]:
        l = right

    # 노드 변경시, 재귀로 다시 업데이트
    if l != idx:
        arr[idx], arr[l] = arr[l], arr[idx]
        heapify(arr, n, l)

print(heap([4,5,2,1,3]))