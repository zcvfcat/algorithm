def binary_search(array, value, left, right):
    if left > right:
        return False

    mid = (left + right) // 2

    if value == array[mid]:
        return mid
    elif value > array[mid]:
        return binary_search(array, value, mid + 1, right)
    elif value < array[mid]:
        return binary_search(array, value, left, mid - 1)


array = [5, 1, 2, 3, 4, 9, 11, 13, 14, 17]
array.sort()

left = 0
right = len(array)

target = 13
count = 0

print(binary_search(array, target, left, right))
