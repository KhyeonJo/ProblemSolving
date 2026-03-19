import sys
input = sys.stdin.readline

A = int(input())
L = list(map(int, input().split()))
dp = [1] * A

for i in range(A):
    for j in range(i):
        if L[j] < L[i]:
            A = dp[j]+1
            if A > dp[i]:
                dp[i] = A
            
print(max(dp))