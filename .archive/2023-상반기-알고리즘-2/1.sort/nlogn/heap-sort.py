def heap_sort(array):
    n = len(array)
    
    # 배열을 최대 힙으로 만듭니다.
    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i)
        
    # 힙에서 하나씩 요소를 꺼내어 정렬합니다.
    for i in range(n - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        heapify(array, i, 0)
        
def heapify(array, n, idx):
    largest = idx
    left = 2 * idx + 1
    right = 2 * idx + 2
    
    # 왼쪽 자식이 루트보다 큰 경우
    if left < n and array[left] > array[largest]:
        largest = left
    
    # 오른쪽 자식이 루트보다 큰 경우
    if right < n and array[right] > array[largest]:
        largest = right
    
    # 루트가 자식보다 작은 경우
    if largest != idx:
        array[idx], array[largest] = array[largest], array[idx]
        heapify(array, n, largest)