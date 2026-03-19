import heapq
import sys
input = sys.stdin.readline

heap = []

N = int(input())
for i in range(N):
    now = int(input())
    if now == 0:
        if not heap:
            print(0)
        else:
            print(-heapq.heappop(heap))
    else:
        heapq.heappush(heap, -now)