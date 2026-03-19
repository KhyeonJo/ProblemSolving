import sys
input = sys.stdin.readline

cnt = 0
n, k = map(int, input().split())
coins = []
for i in range(n):
    coins.append(int(input()))
coins.sort()

dp = [0]*(k+1)
dp[0] = 1

for c in coins:
    for i in range(1, k+1):
        if i-c<0:
            continue
        dp[i] += dp[i-c]
        
print(dp[k])