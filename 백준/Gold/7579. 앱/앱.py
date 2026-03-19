import sys
input = sys.stdin.readline

N, M = map(int, input().split())
mi = list(map(int, input().split())) #용량
ci = list(map(int, input().split())) #비용

knapsack = [[0] * (sum(ci) + 1) for _ in range(N)]

spd = sum(ci)

for i in range(N):
    byte = mi[i]
    cost = ci[i]

    for j in range(sum(ci)):

        if j < cost:
            knapsack[i][j] = knapsack[i-1][j]
        else:
            knapsack[i][j] = max(knapsack[i-1][j], knapsack[i-1][j-cost] + byte)

        if knapsack[i][j] >= M:
            spd = min(spd, j)

print(spd)