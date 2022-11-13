import heapq

N = int(input())

plus_heap = []
minus_heap = []

one = 0
zero = 0

for i in range(N):
    field = int(input())

    if field > 1:
        heapq.heappush(plus_heap, field * -1)
    elif field == 1:
        one += 1
    elif field == 0:
        zero += 1
    else:
        heapq.heappush(minus_heap, field)

total = 0

while len(plus_heap) > 1:
    first = heapq.heappop(plus_heap) * -1
    second = heapq.heappop(plus_heap) * -1
    total += first * second

if len(plus_heap) > 0:
    total += heapq.heappop(plus_heap) * -1

while len(minus_heap) > 1:
    first = heapq.heappop(minus_heap)
    second = heapq.heappop(minus_heap)
    total += first * second

if len(minus_heap) > 0:
    if zero == 0:
        total += heapq.heappop(minus_heap)

total += one

print(total)
