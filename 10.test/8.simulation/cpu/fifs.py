n = int(input('프로세스 수: '))
arrival_time = list(map(int, input('도착시간: ').split()))
burst_time = list(map(int, input('실행시간: ').split()))

start_time, end_time = [], []

for i in range(n):
    if i == 0:
        start_time.append(arrival_time[i])
        end_time.append(start_time[i] + burst_time[i])

    else:
        start_time.append(max(end_time[i - 1], arrival_time[i]))
        end_time.append(start_time[i] + burst_time[i])

total_waiting_time = sum([start_time[i] - arrival_time[i] for i in range(n)])
avg_waiting_time = total_waiting_time / n

print(f"시작시간: {start_time}")
print(f"종료시간: {end_time}")
print(f"평균 대기시간: {avg_waiting_time:.2f} 단위시간")