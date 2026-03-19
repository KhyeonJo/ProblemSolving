import sys
input = sys.stdin.readline

N, K = map(int, input().split())
L = []
for i in range(N):
    L.append(int(input()))

start = 1
end = max(L)

while start <= end: #최대길이로 수렴할 때까지
    mid = (start + end)//2
    cnt = 0
    for i in L:
        cnt += i//mid
    if cnt >= K:
        start = mid+1
    else:
        end = mid-1

print(end)