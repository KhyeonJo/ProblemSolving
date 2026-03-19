import sys
input = sys.stdin.readline

T = int(input())

dp = [0]*(103)
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2

for i in range(T):
    N = int(input())

    if N<6:
        print(dp[N])
    else:
        for j in range(6, N+1):
            if dp[j]!=0:
                continue
            else:
                dp[j] = dp[j-1] + dp[j-5]
        print(dp[N])