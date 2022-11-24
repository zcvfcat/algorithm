# left = 0
# right = 20

# target = 16
# count = 0

# while left <= right:
#     mid = (left + right) // 2
#     count += 1

#     if mid < target:
#         left = mid + 1
#     elif mid > target:
#         right = mid - 1
#     else:
#         break

# print(count)


array = [5, 1, 2, 3, 4, 9, 11, 13, 14, 17]
array.sort()

left = 0
right = len(array)

target = 13
count = 0

while left <= right:
    mid = (left + right) // 2
    value = array[mid]
    count += 1

    if value == target:
        break

    if target > value:
        left = mid + 1
    else:
        right = mid - 1

print(count)
