def heapify(arr, heap_size, root_index):
    largest = root_index
    left_child = 2 * root_index + 1
    right_child = 2 * root_index + 2

    if left_child < heap_size and arr[left_child] > arr[largest]:
        largest = left_child

    if right_child < heap_size and arr[right_child] > arr[largest]:
        largest = right_child

    if largest != root_index:
        arr[root_index], arr[largest] = arr[largest], arr[root_index]
        heapify(arr, heap_size, largest)


def build_heap(arr):
    n = len(arr)

    # 힙을 구성하는 데 필요한 시작 지점을 찾습니다.
    # 마지막 내부 노드부터 시작하여 루트 노드까지 거꾸로 진행합니다.
    # Leaf 노드는 자식 노드가 없으므로 heapify 연산이 필요하지 않습니다. 따라서 leaf 노드부터 시작할 필요가 없습니다.
    # 마지막 내부 노드부터 시작하여 루트 노드까지 거꾸로 진행하면, 각 노드에 대해 heapify 연산을 수행하는 것으로 충분합니다. 이는 효율적인 방법입니다. 왜냐하면 각 내부 노드에 대해 heapify 연산을 수행하면, 해당 노드의 아래쪽에 있는 모든 노드들이 힙의 특성을 만족하게 됩니다.
    # 아래쪽부터 시작하면 상향식으로 힙을 구성할 수 있습니다. 즉, 아래쪽부터 시작하여 각 내부 노드를 최대 힙의 특성을 만족하도록 조정하고, 이를 루트 노드까지 반복적으로 수행함으로써 전체 트리를 최대 힙으로 만들 수 있습니다.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # 최대 힙을 구성한 후, 배열을 정렬합니다.
    for i in range(n - 1, 0, -1):
        # 최대 힙의 최대값을 맨 뒤로 보냅니다.
        arr[0], arr[i] = arr[i], arr[0]
        # 힙의 크기를 줄여 정렬된 부분을 제외하고 나머지 부분에 대해 다시 heapify를 수행합니다.
        heapify(arr, i, 0)

    return arr

# 예제 사용
array = [4, 10, 3, 5, 1]
sorted_array = build_heap(array)
print("정렬된 배열:", sorted_array)