# Segment Tree
class SegmentTree:
    def __init__(self, arr):
        self.arr = arr
        self.tree = [-1] * (2 * len(arr))

    def build(self, node, start, end):
        if start == end:
            self.tree[node] = self.arr[start]
        else:
            mid = (start + end) // 2
            self.build(2 * node, start, mid)
            self.build(2 * node + 1, mid + 1, end)
            self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def query(self, node, start, end, l, r):
        if r < start or end < l:
            return 0
        elif l <= start and end <= r:
            return self.tree[node]
        else:
            mid = (start + end) // 2
            return self.query(2 * node, start, mid, l, r) + self.query(2 * node + 1, mid + 1, end, l, r)

    def update(self, node, start, end, idx, val):
        if start == end:
            self.arr[idx] = val
            self.tree[node] = val
        else:
            mid = (start + end) // 2
            if start <= idx and idx <= mid:
                self.update(2 * node, start, mid, idx, val)
            else:
                self.update(2 * node + 1, mid + 1, end, idx, val)
            self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]


# example
arr = [1, 3, 5, 7, 9, 11]
seg_tree = SegmentTree(arr)
seg_tree.build(1, 0, len(arr) - 1)
print(seg_tree.query(1, 0, len(arr) - 1, 1, 3))  # 16
seg_tree.update(1, 0, len(arr) - 1, 4, 4)
print(seg_tree.query(1, 0, len(arr) - 1, 1, 3))  # 12
