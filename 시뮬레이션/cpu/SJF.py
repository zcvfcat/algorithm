# SJF 알고리즘 구현

# 입력값
processes = [  # 프로세스 리스트
    [0, 4],
    [1, 8],
    [2, 2],
    [3, 6],
    [4, 7]
]

# 초기화
processes.sort(key=lambda x: x[1])  # 각 프로세스를 작업 시간에 따라 오름차순 정렬

# 각 프로세스를 수행하는 루프
total_time = 0  # 총 소요 시간
for process in processes:

    # 현재 프로세스의 작업 시간 더하기
    total_time += process[1]
    print(f'프로세스 {process[0]}의 작업이 {total_time}초에 끝났습니다.')
