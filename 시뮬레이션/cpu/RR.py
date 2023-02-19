def round_robin(processes, quantum):
    # processes는 프로세스 이름과 도착시간이 들어있는 리스트, quantum은 쿼터먼트
    # 초기값은 프로세스 수 n과 프로세스 리스트 p, 잔여시간 리스트 r
    n = len(processes)
    p = processes[:]
    r = [0] * n
    # 프로세스 종료 확인 변수
    done = False
    # 프로세스 실행 결과 저장 변수
    result = []

    # 프로세스가 모두 종료될 때까지 반복
    while not done:
        done = True
        for i in range(n):
            if r[i] > 0:
                # 프로세스가 잔여 시간이 남았다면 프로세스 실행
                done = False
                if r[i] > quantum:
                    # 잔여 시간이 쿼터먼트보다 클 경우 쿼터먼트만큼 실행
                    r[i] -= quantum
                    result.append(p[i])
                else:
                    # 잔여 시간이 쿼터먼트보다 작을 경우 남은 시간만큼 실행
                    result.append(p[i] + " (" + str(r[i]) + ")")
                    r[i] = 0

    # 결과 반환
    return result


# 초기값
processes = [("P1", 2), ("P2", 5), ("P3", 3)]
quantum = 2

# Round-Robin 실행
result = round_robin(processes, quantum)
print(result)
