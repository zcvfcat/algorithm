def quick(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        gt = [x for x in arr[1:] if x >= pivot]

        return quick(less) + [pivot] + quick(gt)
