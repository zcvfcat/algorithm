from queue import Queue

# 각 큐의 우선순위와 시간 할당량, 큐 길이를 지정합니다.
QUEUES = [
    (0, 20, 3),
    (1, 40, 2),
    (2, 60, 1),
]

# 프로세스 리스트를 작성합니다.
processes = [(0, 0), (1, 0), (2, 0)]

def multi_feedback_queue(processes):
    """
    멀티레벨 피드백 큐 알고리즘 함수를 구현합니다.
    """
    # 각 큐를 생성합니다.
    queues = [Queue() for _ in range(len(QUEUES))]
    
    # 프로세스를 초기 큐에 배치합니다.
    for p in processes:
        queues[0].put(p)
    
    # 시작시간을 저장할 변수를 초기화합니다.
    time_start = {p[0]: 0 for p in processes}
    
    # 프로세스들이 실행되는 동안 경과하는 시간입니다.
    elapsed_time = 0
    
    # 모든 큐가 비게될 때까지 루프합니다.
    while queues != []:
        # 현재 실행하고 있는 프로세스입니다.
        current_process = None
        
        # 가장 우선순위가 높은 큐부터 확인합니다.
        for i in range(len(QUEUES)):
            if queues[i].qsize() > 0:
                current_process = queues[i].get()
                
                # 첫 실행인 경우 시작시간을 기록합니다.
                if current_process[1] == 0:
                    time_start[current_process[0]] = elapsed_time
                
                # 실행할 시간을 계산합니다.
                time_to_execute = min(QUEUES[i][1], current_process[1])
                
                # 해당 큐에서 실행합니다.
                for t in range(time_to_execute):
                    elapsed_time += 1
                    current_process = (current_process[0], current_process[1] - 1)
                    
                    # 다음 큐로 이동할 수 있는 경우 이동합니다.
                    if i < len(QUEUES) - 1 and elapsed_time % QUEUES[i][2] == 0:
                        queues[i+1].put(current_process)
                        break
                
                # 실행 완료된 경우 continue 명령을 사용하여 바깥쪽 루프를 다시 실행합니다.
                if current_process[1] == 0:
                    break
            
            # 실행 중인 프로세스가 없는데 마지막 큐인 경우, 처음으로 돌아갑니다.
            elif i == len(QUEUES) - 1 and current_process is None:
                queues[0].put(queues[i].get())
        
        # 다음 프로세스를 실행하기 전에 이전 프로세스의 실행 시간을 거기에 해당하는 리스트  변수에 추가합니다.
        if current_process is not None and current_process[1] > 0:
            next_queue = min(len(QUEUES) - 1, queues.index(max(queues, key=lambda q: q.qsize())) + 1)
            queues[next_queue].put(current_process)
            
        # 큐의 길이가 0인 경우 pop 해 줍니다.
        for q in queues:
            if q.qsize() == 0:
                queues.pop(queues.index(q))
    
    # 결과를 출력합니다.
    for process in processes:
        time_taken = elapsed_time - time_start[process[0]]
        print(f"Process {process[0]} took {time_taken} units of time")
