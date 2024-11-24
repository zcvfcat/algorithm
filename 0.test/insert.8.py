def insert(array):
    for i in range(len(array)):
         # 현재 요소가 이전 요소보다 작다면
        while i > 0 and array[i] < array[i - 1]:
            # 현재 요소와 이전 요소를 교환
            array[i], array[i - 1] = array[i - 1], array[i]
            i -= 1

    return array
