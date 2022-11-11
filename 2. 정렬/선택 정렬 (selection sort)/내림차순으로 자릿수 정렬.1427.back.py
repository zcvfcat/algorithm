array = list(input())

# print(sorted(array, reverse=True))

for i in range(len(array)):
    max_index = i

    for j in range(i + 1, len(array)):
        if array[j] > array[max_index]:
            max_index = j

    array[i], array[max_index] = array[max_index], array[i]

print(''.join(map(str, array)))
