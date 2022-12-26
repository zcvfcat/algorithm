def quick(A, lo, hi):
    def partition(lo, hi):
        pivot = A[hi]
        left = lo

        for right in range(lo, hi):
            if A[right] < pivot:
                A[left], A[right] = A[right], A[left]
                left += 1
        A[left], A[hi] = A[hi], A[left]

        return left

    if lo < hi:
        pivot = partition(lo, hi)
        quick(A, lo, pivot - 1)
        quick(A, pivot + 1, hi)


A = [2, 7, 8, 1, 3, 5, 6, 4, 9]
quick(A, 0, len(A)-1)
print(A)
