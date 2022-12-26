# 불안전한 정렬

def quick(array):
    if len(array) < 2:
        return array

    pivot = array[len(array)//2]
    left, equal, right = [], [], []

    for node in array:
        if node < pivot:
            left.append(node)
        elif node == pivot:
            equal.append(node)
        else:
            right.append(node)

    return quick(left) + equal + quick(right)


array = [5, 3, 2, 4, 1, 6, 7, 8, 9]
print(quick(array))


def quick(A, lo, hi):
    def partition(low, high):  # 로무토 파티션 계획
        pivot = A[high]
        left = low

        for right in range(low, high):
            if A[right] < pivot:
                A[left], A[right] = A[right], A[left]
                left += 1
        A[left], A[high] = A[high], A[left]

        return left

    if lo < hi:
        pivot = partition(lo, hi)
        quick(A, lo, pivot - 1)
        quick(A, pivot + 1, hi)


A = [2, 8, 7, 1, 3, 5, 6, 4]
quick(A, 0, len(A)-1)
print(A)
