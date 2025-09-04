class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, idx):
        return (idx - 1) // 2

    def left_child(self, idx):
        return 2 * idx + 1

    def right_child(self, idx):
        return 2 * idx + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def heapify_up(self, idx):
        while idx > 0 and self.heap[self.parent(idx)] > self.heap[idx]:
            self.swap(self.parent(idx), idx)
            idx = self.parent(idx)

    def heapify_down(self, idx):
        left = self.left_child(idx)
        right = self.right_child(idx)
        smallest = idx

        if left < len(self.heap) and self.heap[left] < self.heap[idx]:
            smallest = left

        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        
        if smallest != idx:
            self.swap(idx, smallest)
            self.heapify_down(smallest)
    
    def push(self, item):
        self.heap.append(item)
        self.heapify_up(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) == 0:
            return None
        
        root = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify_down(0)

        return root

    def peek(self):
        return self.heap[0] if self.heap else None

    def size(self):
        return len(self.heap)


heap = MinHeap()
heap.push(5)
heap.push(7)
heap.push(3)
heap.push(10)

print("Heap 내의 최소값:", heap.peek()) # 3 출력
print("Heap 크기:", heap.size())      # 4 출력

print("Heap에서 pop된 값:", heap.pop())  # 3 출력
print("Heap 내의 최소값:", heap.peek())  # 5 출력
