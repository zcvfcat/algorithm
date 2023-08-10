class MultilevelQueue:
    def __init__(self):
        self.job_queue = []  # 큐 초기화
        self.priority_queues = [[], [], []]  # 우선순위 큐
        self.timeslice = 1  # 할당되는 시간조각
    
    def add_job(self, job):
        self.job_queue.append(job)

    def run_scheduler(self):
        while len(self.job_queue) > 0:
            for i in range(3):  # 각각 생성된 3개의 큐를 순회
                queue = self.priority_queues[i]
                index = 0
                queue_len = len(queue)
                # 해당 우선순위의 작업이 처리중인 상황인지 여부 확인 
                if queue_len > 0 and queue[0].run_time == queue[0].processed_time:
                    # 모든 변수들을 초기화 한다.
                    item = queue.pop(0)
                    print("Job {} has been completed".format(item.id))
                    break

                # 현재 큐가 비어있다면, 다음 큐로 이동한다
                if queue_len == 0:
                    continue

                # 작업 수행
                item = queue.pop(0)
                item.processed_time += self.timeslice                     
                queue.append(item)   # 마지막에 다시 큐에 삽입