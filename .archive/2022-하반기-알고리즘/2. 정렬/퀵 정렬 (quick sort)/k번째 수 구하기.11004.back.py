def quick_sort(unsorted):
    if len(unsorted) <= 1:
        return unsorted

    pivot = unsorted[len(unsorted) // 2]
    lesser_array, equal_array, greater_array = [], [], []

    for number in unsorted:
        if number < pivot:
            lesser_array.append(number)

        elif number > pivot:
            greater_array.append(number)

        else:
            equal_array.append(number)

    return quick_sort(lesser_array) + equal_array + quick_sort(greater_array)


n, k = map(int, input().split(' '))
array = list(map(int, input().split(' ')))

sorted_array = quick_sort(array)

print(sorted_array[k-1])
