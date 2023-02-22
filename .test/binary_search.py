def bs(array, target, left, right):
    if left > right:
        return False

    mid = (left + right) // 2
    assume = array[mid]

    if assume > target:
        return bs(array, target, left, mid - 1)
    elif assume < target:
        return bs(array, target, mid + 1, right)
    else:
        return mid
    
array = [5, 1, 2, 3, 4, 9, 11, 13, 14, 17]
array.sort()

left = 0
right = len(array)

target = 13
count = 0

print(bs(array, target, left, right))

def b(array, target):
    left = 0
    right = len(array) - 1
    
    while left < right:
        mid = (left + right) // 2
        assume = array[mid]

        if assume > target:
            right = mid - 1
        elif assume < target:
            left = mid + 1
        else:
            return mid
    return False

print(b(array, target))