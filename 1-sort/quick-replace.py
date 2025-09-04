def quick_sort_inplace(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    if left < right:
        pivot_index = partition(arr, left, right)
        quick_sort_inplace(arr, left, pivot_index - 1)
        quick_sort_inplace(arr, pivot_index + 1, right)
    return arr

def partition(arr, left, right):
    pivot = arr[right]
    i = left - 1
    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1

# 테스트 코드
if __name__ == "__main__":
    arr = [5, 2, 9, 1, 5, 6, 7, 3]
    print("정렬 전:", arr)
    quick_sort_inplace(arr)
    print("정렬 후:", arr)
