def quick(array):
    if len(array) < 2:
        return array

    pivot = array[len(array) // 2]
    left, equal, right = [], [], []

    for value in array:
        if value < pivot:
            left += [value]
        elif value > pivot:
            right += [value]
        else:
            equal += [value]
    
    return quick(left) + equal + quick(right)