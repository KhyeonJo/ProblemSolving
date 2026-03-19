import sys
input = sys.stdin.readline

N, K = map(int, input().split())
knap = [[0] * (K+1) for i in range(N+1)]
for i in range(1, N+1):
    weight, value = map(int, input().split())
    for j in range(1, K+1):
        if j < weight:
            knap[i][j] = knap[i-1][j]
        else:
            knap[i][j] = max(knap[i-1][j], value + knap[i-1][j-weight])

print(knap[N][K])