array = [5, 3, 2, 4, 1, 6, 7, 8, 9]

end = len(array)
for i in range(end-1, 0, -1):
    for j in range(i):
        if array[j+1] < array[j]:
            array[j+1], array[j] = array[j], array[j + 1]

print(array)


def bubble(a):
    for i in range(1, len(a)):
        for j in range(len(a) - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


print(bubble([1, 23, 4, 1, 24, 23, 2, 3, 53, 4, 234, 2, ]))
