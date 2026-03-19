import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())
INF = float('inf')

queue = []
heapq.heappush(queue, (0, N))

time_values = [INF] * 100001
time_values[N] = 0

while queue:
    current_time, current_pos = heapq.heappop(queue)
    if time_values[current_pos] < current_time:
        continue

    for next_pos, travel_time in [(current_pos+1, 1), (current_pos-1, 1), (current_pos*2, 0)]:
        if 0 <= next_pos < 100001:
            new_time = current_time + travel_time

            if new_time < time_values[next_pos]:
                time_values[next_pos] = new_time
                heapq.heappush(queue, (new_time, next_pos))

print(time_values[K])

