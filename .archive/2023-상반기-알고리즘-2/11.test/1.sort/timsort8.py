unit = 8

def insert(array, start, end):
    for i in range(start + 1, end):
        while start < i and array[i] > array[i - 1]:
            array[i], array[i - 1] = array[i - 1], array[i]
            i -= 1
    return array

def merge(array):
    if len(array) < unit:
        return array
    
    mid = len(array) // 2
    left, right, merged = merge(array[:mid]), merge(array[mid:]), []

    while left and right:
        merged += left.pop(0) if left[0] < right[0] else right.pop(0)

    return merged + left + right


def timsort(array):
    for i in range(0, len(array), unit):
        array = insert(array, i, min(i + unit ,len(array)))

    return merge(array)

    
    
    
