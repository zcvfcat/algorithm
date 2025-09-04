def shell_sort(arr):
    # 셸 정렬은 삽입 정렬을 조금 더 빠르게 만든 정렬 방법이에요.
    # 한 번에 한 칸씩 비교하는 게 아니라, 처음엔 멀리 떨어진 값들끼리 비교해요.
    # 점점 비교하는 간격(gap)을 줄여가면서 정렬해요.

    n = len(arr)
    gap = n // 2  # 처음에는 배열 길이의 절반만큼 떨어진 값들끼리 비교해요.

    while gap > 0:
        # gap만큼 떨어진 값들끼리 삽입 정렬처럼 정렬해요.
        for i in range(gap, n):
            temp = arr[i]
            j = i
            # 앞에 있는 값이 더 크면 뒤로 밀어요.
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp  # 알맞은 자리에 값을 넣어요.
        gap //= 2  # 간격을 반으로 줄여요.

    return arr
