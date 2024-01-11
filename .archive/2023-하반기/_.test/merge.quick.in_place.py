import random

def merge(arr):
    def sort(low, high):
        if high - low < 2:
            return arr[low:high]

        if low < high:
            mid = (low + high) // 2
            sort(low, mid)
            sort(mid,high)
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

def quick(arr):
    def sort(start, end):
        if start >= end:
            return

        pivot = arr[start]
        left = start + 1
        right = end

        while left <= right:
            while left <= end and pivot > arr[left]:
                left += 1

            while pivot < arr[right]:
                right -= 1

            if left <= right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1

        arr[start], arr[right] = arr[right], arr[start]
        sort(start, right - 1)
        sort(left, end)

        return arr

    return sort(0, len(arr) - 1)

array = [random.randint(0, 10) for _ in range(20)]

print(array)
print(quick(array))