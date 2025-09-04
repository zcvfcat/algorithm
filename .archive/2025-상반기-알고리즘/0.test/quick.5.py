# 퀵 정렬, 불안정 정렬
def quick(arr):
    # arr이 2보다 작을 경우 
    if len(arr) < 2:
        return arr
    
    # 일반적으로 정렬된 환경이 있을 케이스가 많아서 중앙값으로 pivot 선택
    pivot = arr[len(arr)//2]
    
    # pivot 보다 작을 케이스와 클 케이스, 같을 케이스 나누어서 저장 공간 생성
    left, right, equal = [], [], []
    
    for v in arr:
        if v < pivot:
            left.append(v)
        elif v > pivot:
            right.append(v)
        else:
            equal.append(v)
    
    return quick(left) + equal + quick(right)