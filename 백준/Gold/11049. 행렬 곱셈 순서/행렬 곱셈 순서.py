import sys
input = sys.stdin.readline

N = int(input())
matAB = []
for i in range(N):
    matAB.append(list(map(int, input().split())))

dp = [[0 for i in range(N)] for j in range(N)]

for length in range(2, N+1):
    for i in range(N - length + 1):
        j = i + length - 1
        dp[i][j] = float('inf')
        for k in range(i, j):
            q = dp[i][k] + dp[k+1][j] + matAB[i][0] * matAB[k][1] * matAB[j][1]
            dp[i][j] = min(dp[i][j], q)

print(dp[0][N-1])