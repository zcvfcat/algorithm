def quick_sort(unsorted):
    if len(unsorted) <= 1:
        return unsorted

    pivot = unsorted[len(unsorted) // 2]
    lesser_lst, equal_lst, greater_lst = [], [], []

    for number in unsorted:
        if number < pivot:
            lesser_lst.append(number)

        elif number > pivot:
            greater_lst.append(number)

        else:
            equal_lst.append(number)

    return quick_sort(lesser_lst) + equal_lst + quick_sort(greater_lst)


unsorted = [5, 8, 4, 6, 7, 1, 9, 3, 2]

sortedArray = quick_sort(unsorted)

print(sortedArray)
