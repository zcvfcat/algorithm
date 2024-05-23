def heapify(arr, n, idx):
    # idx를 루트로 하는 서브트리에서 최대 힙 특성을 유지
    largest = idx
    left = 2 * idx + 1
    right = 2 * idx + 2

    # 왼쪽 자식이 루트보다 크면 왼쪽 자식을 최대값으로 설정
    if left < n and arr[left] > arr[largest]:
        largest = left

    # 오른쪽 자식이 현재 최대값보다 크면 오른쪽 자식을 최대값으로 설정
    if right < n and arr[right] > arr[largest]:
        largest = right

    # 최대값이 루트가 아니면 교환하고 다시 힙 특성을 유지
    if largest != idx:
        arr[idx], arr[largest] = arr[largest], arr[idx]
        heapify(arr, n, largest)


def heap(arr):
    n = len(arr)

    # 배열을 최대 힙으로 변환
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # 하나씩 요소를 힙에서 추출하여 정렬
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # 현재 루트(최대값)과 마지막 요소를 교환
        heapify(arr, i, 0)  # 줄어든 힙에서 루트에 대해 힙 특성 유지

    return arr


# 예제
arr = [4, 10, 3, 5, 1]
sorted_arr = heap(arr)
print(sorted_arr)  # [1, 3, 4, 5, 10]
