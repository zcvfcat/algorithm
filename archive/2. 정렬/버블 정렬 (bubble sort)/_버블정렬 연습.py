'''
max 값을 밀어넣기

특징 : 마지막 경우는 정렬하지 않음
0 - 9 
9, 8, 7, 6, 5, 4, 3, 2
'''

array = [5, 8, 4, 6, 7, 1, 9, 3, 2]
width = len(array)

for i in range(width - 1, 0, -1):
    for j in range(i):

        if array[j] < array[j + 1]:
            continue
        array[j], array[j + 1] = array[j + 1], array[j]

print(array)
