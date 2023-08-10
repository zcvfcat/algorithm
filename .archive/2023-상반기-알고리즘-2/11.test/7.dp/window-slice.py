def window_slice(arr, k):
    max_values = []
    n = len(arr)

    if k <= 0 or k > n:
        return max_values

    for i in range(n - k + 1):
        window_values = arr[i:i + k]
        max_values.append(max(window_values))
    
    return max_values

arr = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(window_slice(arr, k))  # [3, 3, 5, 5, 6, 7]
