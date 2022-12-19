def binary_search(array, value, low, high):
    count = 0

    while low <= high:
        mid = (low + high) // 2
        count += 1

        if value == array[mid]:
            return mid
        elif value > array[mid]:
            low = mid + 1
        elif value < array[mid]:
            high = mid - 1


array = [5, 1, 2, 3, 4, 9, 11, 13, 14, 17]
array.sort()

low = 0
high = len(array)

target = 13
count = 0

print(binary_search(array, target, low, high))
