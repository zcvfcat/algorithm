import heapq

N = int(input())
min_heap = []

for _ in range(N):
    heapq.heappush(min_heap, int(input()))

field_1 = 0
field_2 = 0
total = 0

while len(min_heap) > 1:
    field_1 = heapq.heappop(min_heap)
    field_2 = heapq.heappop(min_heap)
    total += field_1 + field_2
    heapq.heappush(min_heap, field_1 + field_2)

print(total)
