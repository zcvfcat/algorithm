"""
1. 오른쪽으로 가장 작은 수를 찾음
2. 찾은 값의 위치와 스왑
"""

array = [5, 8, 4, 6, 7, 1, 9, 3, 2]
width = len(array)

for i in range(width - 1):
    select_idx = i

    for j in range(i + 1, width):
        if array[j] < array[select_idx]:
            select_idx = j

    array[i], array[select_idx] = array[select_idx], array[i]

print(array)
