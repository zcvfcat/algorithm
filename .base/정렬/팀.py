def binary_search(array, value, left, right):
    if left > right:
        return left

    mid = (left + right) // 2

    if value == array[mid]:
        return mid
    elif value > array[mid]:
        return binary_search(array, value, mid + 1, right)
    elif value < array[mid]:
        return binary_search(array, value, left, mid - 1)

# 작은 array의 경우 작게 정렬 실행


def insertion_sort(array):
    for index in range(1, len(array)):
        value = array[index]
        pos = binary_search(array, value, 0, index - 1)
        array = array[:pos] + [value] + array[pos:index] + array[index+1:]
    return array


def merge(left, right):
    if not left:
        return right

    if not right:
        return left

    if left[0] < right[0]:
        return [left[0]] + merge(left[1:], right)
    else:
        return [right[0]] + merge(left, right[1:])


def tim_sort(array):
    runs, sorted_runs = [], []
    new_run = [array[0]]

    # for every i in the range of 1 to length of array
    for i in range(1, len(array)):
        # if i is at the end of the list
        if i == len(array) - 1:
            new_run.append(array[i])
            runs.append(new_run)
            break
        # if the i'th element of the array is less than the one before it
        if array[i] < array[i-1]:
            # if new_run is set to None (NULL)
            if not new_run:
                runs.append([array[i]])
                new_run.append(array[i])
            else:
                runs.append(new_run)
                new_run = []
        # else if its equal to or more than
        else:
            new_run.append(array[i])

    # for every item in runs, append it using insertion sort
    for item in runs:
        sorted_runs.append(insertion_sort(item))

    # for every run in sorted_runs, merge them
    sorted_array = []
    for run in sorted_runs:
        sorted_array = merge(sorted_array, run)

    return sorted_array


print(tim_sort([2, 3, 5, 6, 7, 4, 8, 9]))
