def round_robin(processes, quantum):
    """
    :param processes: 프로세스 리스트 [(pid1, arrival_time1, burst_time1), (pid2, arrival_time2, burst_time2), ...]
    :param quantum: 프로세스가 실행될 최대 시간 단위
    :return: (avg_turnaround_time, avg_waiting_time)
    """
    n = len(processes)  # 총 프로세스 개수
    burst_times = {p[0]: p[2] for p in processes}  # process id를 key로 하여, 각 프로세스의 burst time을 value로 저장

    # 각 프로세스에 대한 정보 저장
    turn_times = {}  # 각 프로세스의 turnaround time을 저장할 딕셔너리
    wait_times = {}  # 각 프로세스의 waiting time을 저장할 딕셔너리
    current_time = 0  # 현재 시간

    while True:
        done = True   # 모든 프로세스가 끝나면 while문 종료
        for i in range(n):
            pid, arrival_time, burst_time = processes[i]
            if burst_times[pid] > 0:   # 해당 프로세스가 아직 실행되지 않았으면
                done = False   # 작업중인 프로세스가 하나라도 있다면 done 변수는 False
                if burst_times[pid] > quantum:
                    # 해당 프로세스가 quantum보다 큰 burst time을 가진다면
                    current_time += quantum  # 실행을 위해 상수 할당 ex) q=2 -> cpu 사용량 2 증가하였음을 표기
                    burst_times[pid] -= quantum  # 해당 프로세스의 burst time에서 quantum만큼 차감
                else:
                    # 해당 프로세스가 quantum 이하의 burst time을 가진다면
                    current_time += burst_times[pid]  # 해당 프로세스의 남은 burst time 만큼 cpu 사용
                    wait_times[pid] = current_time - arrival_time - burst_times[pid] # 해당 프로세스의 waiting time 설정
                    burst_times[pid] = 0   # 해당 프로세스의 모든 burst time을 사용하였으므로 0으로 설정

                    # 해당 프로세스의 turnaround time을 결정하고, turn_times 딕셔너리에 저장
                    turn_times[pid] = current_time - arrival_time

        if done:
            break

    # 평균 turnaround time과 평균 waiting time을 계산하여 반환
    avg_turnaround_time = sum(turn_times.values()) / n   
    avg_waiting_time = sum(wait_times.values()) / n   

    return avg_turnaround_time, avg_waiting_time

processes = [(1, 0, 10), (2, 1, 4), (3, 2, 2), (4, 3, 1)]
quantum = 3

print(round_robin(processes, quantum))