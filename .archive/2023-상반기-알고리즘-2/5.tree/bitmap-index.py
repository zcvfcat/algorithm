def create_bitmap_index(lst): 
    # 각 원소를 인덱스로 하고 0으로 초기화한 리스트 생성
    bitmap_lst = [0] * max(lst)

    # 리스트의 원소들을 인덱스로 하고 값을 1로 변경
    for i in lst:
        bitmap_lst[i-1] = 1
    return bitmap_lst

# 입력 리스트
lst = [1, 2, 4, 5, 6]

# 출력
bitmap_lst = create_bitmap_index(lst)
print(bitmap_lst)

# 출력결과
[1, 1, 1, 0, 1, 1]