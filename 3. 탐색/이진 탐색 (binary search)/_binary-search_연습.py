unsorted = [5, 8, 4, 6, 7, 1, 9, 3, 2]
array = sorted(unsorted)

start = 0
end = len(array) - 1
target = 3
is_find = True

while start <= end and not is_find:
    mid = (start + end)// 2
    mid_value = array[mid]

    if mid_value > target:
        end = mid - 1
    elif mid_value < target:
        start = mid + 1
    else:
        is_find = True

print(is_find)