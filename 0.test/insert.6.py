def insert(array:list[int]):
    for i in range(len(array)):
        while i > 0 and array[i] < array[i - 1]:
            array[i], array[i - 1] = array[i - 1], array[i]
            i -= 1
    return array

print(insert([5, 2, 4, 6, 1, 3]))