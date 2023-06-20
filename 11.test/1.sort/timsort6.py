def insert_sort(array, start, end):
    for idx in range(start, end):
        while idx > start and array[idx] < array[idx - 1]:
            array[idx - 1], array[idx] = array[idx], array[idx - 1]
            idx -= 1
    return array


def timsort(array, unit = 32):
    # 단위 쪼개기
    for start in range(len(array), unit):
        array = insert_sort(array, start, min(start + unit, len(array)))
    
