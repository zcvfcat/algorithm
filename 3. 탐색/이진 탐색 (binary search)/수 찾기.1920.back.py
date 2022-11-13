n = int(input())
a = list(map(int, input().split(' ')))

m = int(input())
target_array = list(map(int, input().split(' ')))

a.sort()

for i in range(m):
    is_find = False
    target = target_array[i]

    start = 0
    end = len(a) - 1

    while start <= end:
        mid_index = (start + end) // 2
        mid_value = a[mid_index]

        if mid_value > target:
            end = mid_index - 1
        elif mid_value < target:
            start = mid_index + 1
        else:
            is_find = True
            break

    if is_find is True:
        print(1)
    else:
        print(0)
