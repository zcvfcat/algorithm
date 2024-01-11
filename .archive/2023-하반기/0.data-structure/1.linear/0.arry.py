"""
    배열
        요소들을 연속적으로 저장하는 선형 자료구조
"""


class Array:
    def __init__(self, capacity):
        self.capacity = capacity
        self.arr = [None] * capacity

    def get(self, index):
        if 0 <= index < self.capacity:
            return self.arr[index]
        else:
            return None

    def set(self, index, value):
        if 0 <= index < self.capacity:
            self.arr[index] = value
        else:
            raise IndexError("Index out of bounds")

    def length(self):
        return len(self.arr)
