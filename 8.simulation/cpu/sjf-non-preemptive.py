def sjf_non_preemptive(processes):
    n = len(processes)
    burst_time = [processes[i][1] for i in range(n)]
    wt = [0] * n
    tat = [0] * n

    # 구조체 내에서 가장 짧은 프로세스를 선택합니다.
    shortest = 0 
    for i in range(1, n): 
        if burst_time[i] < burst_time[shortest]: 
            shortest = i 

    # 짧은 시간 순서대로 프로세스를 실행합니다.
    time = processes[shortest][1]
    for i in range(n):
        if processes[i][1] == burst_time[shortest]:
            tat[i] = time - processes[i][0]
            wt[i] = tat[i] - processes[i][1]

            # 모든 프로세스가 종료되면 처리를 중지합니다.
            if i == n - 1:
                return (wt, tat)

            # 다음 가장 짧은 프로세스를 선택합니다.
            shortest = i + 1
            for j in range(i + 2, n):
                if burst_time[j] < burst_time[shortest]:
                    shortest = j

        time += processes[shortest][1]

    return (wt, tat)