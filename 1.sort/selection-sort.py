import random

def selection(array):
    for node in range(len(array)):
        select = node

        for idx in range(node, len(array)):
            if array[select] > array[idx]:
                select = idx
        
        array[select], array[node] = array[node], array[select]

    return array


array = [random.randint(0, 10) for _ in range(20)]
print(array)
print(selection(array))