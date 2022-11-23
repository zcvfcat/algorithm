array = [5, 3, 2, 4, 1, 6, 7, 8, 9]

end = len(array)
for i in range(end-1, 0, -1):
    for j in range(i):
        if array[j+1] < array[j]:
            array[j+1], array[j] = array[j], array[j + 1]

print(array)
