def quick(array):
    if len(array) < 2:
        return array
    
    pivot = array[len(array)//2]
    left, equal,right = [],[],[]

    for val in array:
        if val < pivot:
            left.append(val)
        elif val > pivot:
            right.append(val)
        else:
            equal.append(val)

    return quick(left) + equal + quick(right)

arr = [5, 4, 3, 2, 1, 6, 7, 8, 9]
print(quick(arr))