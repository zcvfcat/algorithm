"""
min(왼쪽, 오른쪽) 작은 값을 왼쪽으로 밀어넣음
"""
array = [5, 8, 4, 6, 7, 1, 9, 3, 2]
width = len(array)

for end in range(1, width):
    for idx in range(end, 0, - 1):

        if array[idx - 1] < array[idx]:
            continue

        array[idx - 1], array[idx] = array[idx], array[idx - 1]

print(array)
