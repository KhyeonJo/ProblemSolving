import sys
input = sys.stdin.readline

N = int(input())
L = []
for i in range(N):
    L.append(int(input()))

dp = [0]*(N+1)
dp[0] = L[0]
if N>1:
    dp[1] = dp[0] + L[1]
if N>2:
    dp[2] = max(L[0]+L[2],L[1]+L[2])
if N>3:
    dp[3] = max(dp[1]+L[3], dp[0]+L[2]+L[3])

for i in range(4, N):
    A = dp[i-2]+L[i]
    B = dp[i-3]+L[i-1]+L[i]
    C = dp[i-4]+L[i-1]+L[i]
    dp[i] = max(A, B, C)

print(max(dp))