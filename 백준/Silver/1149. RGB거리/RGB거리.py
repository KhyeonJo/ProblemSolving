import sys

input = sys.stdin.readline
N = int(input())
pays = []
for i in range(N):
    pays.append(list(map(int, input().split())))

dp = [[0]*3 for i in range(N)]
dp[0] = pays[0]

for i in range(1, N): #dp[i][012]가 RGB임. 가장 최근 선택한 RGB가 그 2차 idx.
    dp[i][0] = min(dp[i-1][1:]) + pays[i][0]
    dp[i][1] = min(dp[i-1][0:3:2]) + pays[i][1]
    dp[i][2] = min(dp[i-1][:2]) + pays[i][2]

print(min(dp[-1]))