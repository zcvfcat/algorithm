def quick_sort(unsorted):
    if len(unsorted) <= 1:
        return unsorted

    pivot = unsorted[len(unsorted) // 2]
    lesser, equal, greater = [], [], []

    for number in unsorted:
        if number < pivot:
            lesser.append(number)

        elif number > pivot:
            greater.append(number)

        else:
            equal.append(number)

    return quick_sort(lesser) + equal + quick_sort(greater)


unsorted = [5, 8, 4, 6, 7, 1, 9, 3, 2]

sorted_array = quick_sort(unsorted)

print(sorted_array)
