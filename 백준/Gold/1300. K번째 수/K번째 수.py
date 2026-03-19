import sys

input = sys.stdin.readline

N = int(input())
k = int(input())

start, end = 1, N*N
while start<=end: #BTS
    mid = (start+end) // 2
    result = 0
    
    for i in range(1, N+1): #검색기준값 연산
        result += min(mid // i, N)

    if result >= k: #판단
        end = mid - 1
        ans = mid
    else:
        start = mid + 1

print(ans)
