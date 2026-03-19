import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    N = int(input())
    files = list(map(int, input().split()))

    prefix = [0] * (N+1)
    for j in range(N):
        prefix[j+1] = files[j] + prefix[j]

    dp = [[0] * N for _ in range(N)]

    for length in range(2, N+1):        # 구간 길이
        for i in range(N - length + 1):
            j = i - 1 + length
            res = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + prefix[j + 1] - prefix[i]
                if cost < res:
                    res = cost
            dp[i][j] = res


    print(dp[0][N-1])