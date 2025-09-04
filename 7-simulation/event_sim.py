import heapq


class EventSimulator:
    """
    간단한 이벤트 기반 시뮬레이터.
    - 시간(time) 순으로 이벤트를 처리합니다.
    - 이벤트는 (time, id, callback) 형태로 스케줄링합니다.
    """

    def __init__(self):
        self.time = 0
        self.pq = []
        self._auto_id = 0

    def schedule(self, time, callback):
        """time 시각에 callback 함수를 실행하도록 스케줄링"""
        heapq.heappush(self.pq, (time, self._auto_id, callback))
        self._auto_id += 1

    def run(self):
        """이벤트가 남지 않을 때까지 실행"""
        while self.pq:
            time, _eid, cb = heapq.heappop(self.pq)
            self.time = time
            cb(self)


