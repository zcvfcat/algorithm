array = [5, 3, 2, 4, 1, 6, 7, 8, 9]

for end in range(1,len(array)):
    for idx in range(end, 0, - 1):

        if array[idx - 1] < array[idx] :
            continue

        array[idx - 1], array[idx] = array[idx], array[idx - 1]

print(array)