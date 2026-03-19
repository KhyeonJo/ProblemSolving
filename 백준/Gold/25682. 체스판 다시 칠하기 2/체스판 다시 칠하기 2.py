import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
MB = [input().strip() for _ in range(N)]

Bbd = [[0 for _ in range(M+1)] for _ in range(N+1)]
Wbd = [[0 for _ in range(M+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        if (i+j)%2:
            if MB[i-1][j-1]=='W':
                Bbd[i][j] = Bbd[i-1][j] + Bbd[i][j-1] - Bbd[i-1][j-1]
                Wbd[i][j] = 1 + Wbd[i-1][j] + Wbd[i][j-1] - Wbd[i-1][j-1]
            else:
                Bbd[i][j] = 1 + Bbd[i-1][j] + Bbd[i][j-1] - Bbd[i-1][j-1]
                Wbd[i][j] = Wbd[i-1][j] + Wbd[i][j-1] - Wbd[i-1][j-1]
        else:
            if MB[i-1][j-1]=='B':
                Bbd[i][j] = Bbd[i-1][j] + Bbd[i][j-1] - Bbd[i-1][j-1]
                Wbd[i][j] = 1 + Wbd[i-1][j] + Wbd[i][j-1] - Wbd[i-1][j-1]
            else:
                Bbd[i][j] = 1 + Bbd[i-1][j] + Bbd[i][j-1] - Bbd[i-1][j-1]
                Wbd[i][j] = Wbd[i-1][j] + Wbd[i][j-1] - Wbd[i-1][j-1]
ans = 2000000

for i in range(K, N+1):
    for j in range(K, M+1):
        B_sub = Bbd[i][j] - Bbd[i-K][j] - Bbd[i][j-K] + Bbd[i-K][j-K]
        W_sub = Wbd[i][j] - Wbd[i-K][j] - Wbd[i][j-K] + Wbd[i-K][j-K]
        ans = min(ans, B_sub, W_sub)

print(ans)