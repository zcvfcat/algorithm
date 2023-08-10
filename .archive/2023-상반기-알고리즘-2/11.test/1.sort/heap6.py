def heap(arr):
    length = len(arr)

    for idx in range(length // 2 - 1, - 1, -1):
        heapify(arr, length, idx)

    for i in range(length - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

# 최대 힙
def heapify(arr, length, idx):
    curr = idx
    left = 2 * idx + 1 # 왼쪽 leaf
    right = 2 * idx + 2 # 오른쪽 leaf

    # leaf 비교
    if left < length and arr[left] > arr[curr]:
        curr = left

    if right < length and arr[right] > arr[curr]:
        curr = right

    # 만약 자리가 바뀐다면 하위 트리까지 확인
    if curr != idx:
        arr[idx], arr[curr] = arr[curr], arr[idx]
        heapify(arr, length, curr)
