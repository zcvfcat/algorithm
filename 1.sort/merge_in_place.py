import random


def merge(arr):
    def sort(low, high):
        if high - low < 2:
            return arr[low: high]

        if (low < high):
            mid = (low + high) // 2
            sort(low, mid)
            sort(mid, high)
            merge(low, mid, high)

        return arr

    def merge(low, mid, high):
        left, right = arr[low:mid], arr[mid:high]
        merged = []

        while left and right:
            if left[0] < right[0]:
                merged.append(left.pop(0))
            else:
                merged.append(right.pop(0))
        
        arr[low:high] = merged + left + right

    return sort(0, len(arr))


array = [random.randint(0, 10) for _ in range(20)]
print(array)
print(merge(array))
