def shell_sort(arr):
    n = len(arr)
    gap = n // 2 # 초기 gap 설정

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            # 부분적으로 정렬된 리스트의 작은 값들이 앞에 오도록 세부 정렬
            while j >= gap and arr[j-gap] > temp:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp # 확정 위치에 하나씩 넣어줌
        gap //= 2 # gap 감소
            
    return arr

print(shell_sort([5,1,3,2,4]))