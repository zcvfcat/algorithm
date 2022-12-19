array = [5, 3, 2, 4, 1, 6, 7, 8, 9]

for i in range(len(array)):
    select_idx = i
    for j in range(i + 1, len(array)):
        if array[select_idx] > array[j]:
            select_idx = j

    array[select_idx], array[i] = array[i], array[select_idx]

print(array)
