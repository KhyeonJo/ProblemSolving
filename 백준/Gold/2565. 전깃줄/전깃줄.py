import sys
input = sys.stdin.readline

N = int(input())
L = []
for i in range(N):
    L.append(list(map(int, input().split())))

L.sort()

dp = [1] * N

for i in range(N):
    for j in range(i):
        if L[i][1] > L[j][1]:
            dp[i] = max(dp[i], dp[j]+1)

print(N - max(dp))




#dp[i]는 sort한 L에서 i번째 값까지 한번도 안교차되고 
#가능한 최대 길이의 수열(선 개수)