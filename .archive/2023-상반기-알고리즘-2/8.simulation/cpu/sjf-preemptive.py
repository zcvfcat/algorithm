from collections import deque  # deque 사용 

class Process:
    def __init__(self, name, arrive_time, burst_time):
        self.name = name
        self.arrive_time = arrive_time
        self.burst_time = burst_time

def sjf_preemptive(processes):
    current_p = None  # current process
    clock = 0  # 시간 체크용 총 클락수 
    wait_times = []  # wait time 기록할 list 
    ready_q = deque()  # 대기열 (큐) 

    while processes or ready_q:
        # ready queue에 들어올 시간이 되면 processes 리스트에서 ready queue로 이동
        arrived_p = [p for p in processes if p.arrive_time == clock]
        for p in arrived_p:
            ready_q.append(p)
            processes.remove(p)

        
        if current_p and current_p.burst_time == 0: 
            # 1. 현재 수행하고 있는 프로세서의 burst_time이 0이 되면 종료 
            wait_times.append(clock - current_p.arrive_time - current_p_tm)
            current_p = None

        if not current_p:
            # 2. 진입한 프로세서가 없다면, 대기열에서 가장 burst time 짧은 프로세서 선택 및 수행 
            if ready_q:
                shortest_job = min(ready_q, key=lambda x: x.burst_time)
                ready_q.remove(shortest_job)
                current_p = shortest_job
                current_p_tm = 0
        
        else:   # 3. 그 외에는 소요시간 1 tick 감소
            current_p.burst_time -= 1
            current_p_tm += 1
            
            #대기열에 burst time이 더 작은 프로세서가 있으면 current switch
            for p in ready_q:
                if p.burst_time < current_p.burst_time and p.arrive_time <= clock:
                    ready_q.remove(p)
                    ready_q.append(current_p)
                    current_p = p
                    current_p_tm = 0
        
        clock += 1  # 시간 체크

    return sum(wait_times) / len(wait_times)