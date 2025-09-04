def merge_sort_top_down(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort_top_down(arr[:mid])
    right = merge_sort_top_down(arr[mid:])
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# 테스트 코드
if __name__ == "__main__":
    arr = [5, 2, 9, 1, 5, 6, 7, 3]
    print("정렬 전:", arr)
    sorted_arr = merge_sort_top_down(arr)
    print("정렬 후:", sorted_arr)

