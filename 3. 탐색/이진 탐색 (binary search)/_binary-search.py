unsorted = [5, 8, 4, 6, 7, 1, 9, 3, 2]
sorted_array = sorted(unsorted)

start = 0
end = len(sorted_array) - 1
target = 3
is_find = False

while start <= end and not is_find:
    mid_index = (start + end) // 2
    mid_value = sorted_array[mid_index]

    if mid_value > target:
        end = mid_index - 1
    elif mid_value < target:
        start = mid_index + 1
    else:
        is_find = True

print(is_find)
