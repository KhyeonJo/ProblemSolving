import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())
jewels = [list(map(int, input().split())) for i in range(N)]
bags = [int(input()) for i in range(K)]
jewels.sort()
bags.sort()

result = 0
possible_jewels = [] #용량 낮은 가방부터 기준으로 쭉 돌면서 가능한 jewel수집

for bag in bags:
    while jewels and bag>=jewels[0][0]:
        heapq.heappush(possible_jewels, (-jewels[0][1], jewels[0][0]))
        heapq.heappop(jewels)
    if possible_jewels:
        result -= heapq.heappop(possible_jewels)[0]
    
print(result)