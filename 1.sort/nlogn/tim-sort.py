def insertion_sort(arr, left, right):
    """
    A simple implementation of insertion sort
    """
    for i in range(left+1, right+1):
        key_item = arr[i]
        j = i - 1
        while j >= left and arr[j] > key_item:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key_item

def merge(arr, start, midpoint, end):
    """
    Merge function for merging two sorted runs
    """
    first_half = arr[start:midpoint+1]
    last_half = arr[midpoint+1:end+1]
    merged_arr, i, j = [], 0, 0

    while (i < len(first_half) and j < len(last_half)):
        if (first_half[i] < last_half[j]):
            merged_arr.append(first_half[i])
            i += 1
        else:
            merged_arr.append(last_half[j])
            j += 1

    merged_arr += first_half[i:]
    merged_arr += last_half[j:]

    return merged_arr

def tim_sort(arr):
    """
    Tim Sort algorithm implementation
    """
    # define a minimum run
    min_run = 32
    n = len(arr)
    
    # Insertion sort on the runs created
    for i in range(0, n, min_run):
        insertion_sort(arr, i, min((i+min_run-1), n-1))
        
    # merge the sorted runs
    size = min_run
    while(size < n):
        for start in range(0, n, size*2):
            midpoint = start + size - 1
            end = min((start + size*2 - 1), (n-1))
            merged_arr = merge(arr, start, midpoint, end)
            arr[start:start+len(merged_arr)] = merged_arr
        size *= 2
    
    return arr

# Test the above implemented Tim sort algorithm
arr = [5, 21, 7, 23, 19]
print(tim_sort(arr))