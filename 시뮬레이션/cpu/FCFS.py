# FCFS 알고리즘을 사용한 프로세스 스케줄링

# 프로세스 도착 시간 리스트
arrival_time = [0, 2, 4, 5]

# 프로세스 소요 시간 리스트
burst_time = [3, 6, 4, 2]

# 각 프로세스의 실행 시간 리스트
execution_time = [0] * len(arrival_time)

# 각 프로세스의 종료 시간 리스트
completion_time = [0] * len(arrival_time)

# 프로세스 스케줄링을 수행합니다.
for i in range(len(arrival_time)):
    # 현재 실행 중인 프로세스가 없을 때
    if i == 0:
        execution_time[i] = burst_time[i]
    # 현재 실행 중인 프로세스가 있을 때
    else:
        # 프로세스 종료 시간을 계산합니다.
        completion_time[i-1] = execution_time[i-1]
        # 프로세스 실행 시간을 계산합니다.
        execution_time[i] = completion_time[i-1] + burst_time[i]

# 각 프로세스의 실행 시간과 종료 시간을 출력합니다.
for i in range(len(arrival_time)):
    print("Process {} :".format(i + 1))
    print("\tArrival Time: {}".format(arrival_time[i]))
    print("\tBurst Time: {}".format(burst_time[i]))
    print("\tExecution Time: {}".format(execution_time[i]))
    print("\tCompletion Time: {}".format(completion_time[i]))
    print()
