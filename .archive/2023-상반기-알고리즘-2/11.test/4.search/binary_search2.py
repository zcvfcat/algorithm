def binary_search(array, target):
    array.sort()
    start = 0
    end = len(array)

    while start < end:
        mid = (start + end) // 2 
        value = array[mid]

        if value < target:
            start = mid + 1
        elif value > target:
            end = mid - 1
        else:
            return mid
    
    return None
array = [0, 1, 3, 6, 7, 8, 8, 9]
print(binary_search(array, 8))