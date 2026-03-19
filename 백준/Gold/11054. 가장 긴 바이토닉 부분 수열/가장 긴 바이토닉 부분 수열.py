import sys
input = sys.stdin.readline

N = int(input())
seq = list(map(int, input().split()))
rev_seq = seq[::-1]

dp = [1] * (N+1)
rev_dp = [1] * (N+1)

for i in range(N):
    for j in range(i):
        if seq[i] > seq[j]:
            A = dp[j] + 1
            if A > dp[i]:
                dp[i] = A
        if rev_seq[i] > rev_seq[j]:
            A = rev_dp[j] + 1
            if A > rev_dp[i]:
                rev_dp[i] = A

ans = 0
for i in range(N):
    A = dp[i] + rev_dp[N-i-1] - 1
    if A > ans:
        ans = A
        
print(ans)