unsorted = [5, 8, 4, 6, 7, 1, 9, 3, 2]
array = sorted(unsorted)

start = 0
end = len(unsorted) - 1
target = 3
is_find = False

while start <= end and is_find is False:
    mid = (start + end) // 2
    value = array[mid]

    if value > target:
        end = mid - 1
    elif value < target:
        start = mid + 1
    else:
        is_find = True

print(is_find)
