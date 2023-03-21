def bs(array, target):
    array.sort()
    left, right = 0, len(array) - 1

    while left <= right:
        mid = (left + right) // 2
        
        if array[mid] < target:
            left = mid + 1
        elif array[mid] > target:
            right = mid - 1
        else:
            return mid

def bsr(array, target, left, right):
    if left > right:
        return None
    
    mid = (left + right) // 2

    if array[mid] < target:
        return bsr(array, target, mid + 1, right)
    elif array[mid] > target:
        return bsr(array, target, left, mid - 1)
    else:
        return mid
    
array = [0, 1, 3, 6, 7, 8, 9]
print(bs(array, 8))
print(bsr(sorted(array), 8, 0, len(array)))