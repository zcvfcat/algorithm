def timsort(arr):
    n = len(arr)  # 배열 길이
    # 배열의 길이가 32보다 작으면 Insertion Sort로 바로 정렬한다.
    if n <= 32:
        ins_sort(arr)
    # 배열을 반으로 나눈다.
    else:
        mid = n // 2
        # left 배열
        L = arr[:mid]
        # right 배열
        R = arr[mid:]
        # left 배열과 right 배열을 재귀적으로 다시 반으로 나눈다.
        timsort(L)
        timsort(R)
        # 반으로 나뉜 배열들을 다시 합병한다.
        merge(arr, L, R)

    return arr

# 배열을 반으로 나눈 후 합병하는 함수


def merge(arr, L, R):
    # 두 배열의 길이를 각각 저장해 놓는다.
    nL = len(L)
    nR = len(R)
    # 새로운 배열을 만들어 준다.
    arr2 = [0] * (nL + nR)
    i = j = k = 0

    # 두 배열을 비교하여 작은 값을 새로운 배열에 넣어준다.
    while i < nL and j < nR:
        if L[i] < R[j]:
            arr2[k] = L[i]
            i += 1
        else:
            arr2[k] = R[j]
            j += 1
        k += 1

    # 남은 데이터를 새로운 배열에 넣어준다.
    while i < nL:
        arr2[k] = L[i]
        i += 1
        k += 1
    while j < nR:
        arr2[k] = R[j]
        j += 1
        k += 1

    # 새로 정렬된 배열을 원래 배열에 넣어준다.
    for i in range(nL + nR):
        arr[i] = arr2[i]

# Insertion Sort 함수


def ins_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


arr = [5, 4, 3, 2, 1, 6, 7, 8, 9]
print(timsort(arr))
