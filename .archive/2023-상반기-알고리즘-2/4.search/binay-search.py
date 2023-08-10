def binarySearch(array,target):
    array.sort()
    start, end = 0, len(array)

    while start <= end:
        mid = (start + end) // 2

        if array[mid] < target:
            start = mid + 1
        elif array[mid] > target:
            end = mid - 1
        else:
            return mid        
        
    return False

array = [0, 1, 3, 6, 7, 8, 9]
print(binarySearch(sorted(array), 8))