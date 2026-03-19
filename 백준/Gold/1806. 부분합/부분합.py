import sys
input = sys.stdin.readline

N, S = map(int, input().split())
L = list(map(int, input().split()))

len = N+1

start, end = 0, 0

now_sum = L[0]
while end!=N:
    if now_sum >= S:
        if (end-start) < len:
            len = end - start + 1
        start +=1
        now_sum -= L[start-1]
    else:
        end +=1
        if end!=N:
            now_sum += L[end]


if len == N+1:
    print(0)
else:
    print(len)