def merge(array):
    if len(array) < 2:
        return array

    mid = len(array) // 2
    left = merge(array[:mid])
    right = merge(array[mid:])

    ans = []

    while left and right:
        if left[0] < right[0]:
            ans.append(left.pop(0))
        elif left[0] > right[0]:
            ans.append(right.pop(0))
    
    ans += left
    ans += right

    return ans

arr = [5, 4, 3, 2, 1, 6, 7, 8, 9]
print(merge(arr))

    