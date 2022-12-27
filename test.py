def sort_array(source_array):
    odd_index = []
    even_index = []

    odds = []
    evens = []

    for i, v in enumerate(source_array):
        if v % 2 == 1:
            odds.append(v)
            odd_index.append(i)
        else:
            evens.append(v)
            even_index.append(i)

    odds.sort()

    s = []
    while True:
        if odd_index and even_index:
            if odd_index[0] < even_index[0]:
                odd_index.pop(0)
                s.append(odds.pop(0))
            else:
                even_index.pop(0)
                s.append(evens.pop(0))
        elif odd_index:
            s.extend(odds)
            break
        else:
            s.extend(evens)
            break
    print(s)
    return s


sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]
