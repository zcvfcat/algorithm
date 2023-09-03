"""
    Heap
        특정 순서로 정렬된 원소들을 효율적으로 관리하는 자료구조로, 최소값 또는 최대값
    
    시간 복잡도
        삽입(insertion): O(log n)
            원소를 힙에 삽입할 때, 일반적으로 힙의 특성을 유지하기 위해 로그 시간 복잡도가 소요
            이는 새로운 원소를 힙의 말단에 추가한 후, 부모 노드와 비교하면서 적절한 위치로 이동시키는 과정
        최소/최대 값 추출(extract min/max): O(log n)
            최소 힙에서 최소값을 추출하거나 최대 힙에서 최대값을 추출하는 연산은 힙의 특성을 유지하기 위해 로그 시간 복잡도가 소요
        최소/최대 값 확인(get min/max): O(1)
            최소 힙 또는 최대 힙에서 가장 작은 또는 가장 큰 값을 확인하는 연산은 상수 시간 복잡도를 가집니다. 추출하지 않고 단순히 값을 확인

    사용 이유
        최소값 또는 최대값 추출
        힙 정렬
            최소값, 최대값을 반복적으로 추출하여 정렬
        다익스트라 알고리즘
            최단 경로를 찾는 다익스트라에서
        프림 알고리즘
            최소 스패닝 트리를 찾는 프림 알고리즘에서 최소 힙이 사용
        태스크 스케줄링
            작업의 우선순위를 관리하기 위해 힙을 사용
"""


class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, item):
        """
        힙에 원소를 삽입합니다.

        :param item: 삽입할 원소
        """
        self.heap.append(item)
        self._heapify_up(len(self.heap) - 1)

    def extract_min(self):
        """
        힙에서 최소값을 추출하고 반환합니다.

        :return: 최소값
        """
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def _heapify_up(self, index):
        """
        지정된 인덱스 위치의 원소를 힙의 올바른 위치로 이동시킵니다.

        :param index: 원소의 인덱스
        """
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] >= self.heap[parent_index]:
                break
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index

    def _heapify_down(self, index):
        """
        지정된 인덱스 위치의 원소를 힙의 올바른 위치로 이동시킵니다.

        :param index: 원소의 인덱스
        """
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            smallest = index

            if (
                left_child_index < len(self.heap)
                and self.heap[left_child_index] < self.heap[smallest]
            ):
                smallest = left_child_index
            if (
                right_child_index < len(self.heap)
                and self.heap[right_child_index] < self.heap[smallest]
            ):
                smallest = right_child_index

            if smallest == index:
                break

            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            index = smallest

    def get_min(self):
        """
        힙에서 최소값을 반환하되 추출하지 않습니다.

        :return: 최소값
        """
        if len(self.heap) > 0:
            return self.heap[0]
        return None

    def is_empty(self):
        """
        힙이 비어있는지 여부를 반환합니다.

        :return: 비어있으면 True, 아니면 False
        """
        return len(self.heap) == 0

    def __str__(self):
        """
        힙의 내용을 문자열로 반환합니다.
        """
        return str(self.heap)


# 최소 힙 인스턴스 생성
min_heap = MinHeap()

# 원소 삽입
min_heap.insert(5)
min_heap.insert(10)
min_heap.insert(3)
min_heap.insert(7)
min_heap.insert(1)

# 최소값 추출
print("Extracted Min:", min_heap.extract_min())

# 최소값 확인 (추출하지 않음)
print("Min:", min_heap.get_min())

# 힙 내용 출력
print("Heap:", min_heap)
