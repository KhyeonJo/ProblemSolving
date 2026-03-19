import sys
input = sys.stdin.readline
s1 = input().strip()
s2 = input().strip()


lcs_dp = [[0 for i in range(len(s2)+1)] for j in range(len(s1)+1)]

for i in range(1, len(s1)+1):
    for j in range(1, len(s2)+1):
        if s1[i-1] == s2[j-1]:
            lcs_dp[i][j] = lcs_dp[i-1][j-1] + 1
        else:
            lcs_dp[i][j] = max(lcs_dp[i-1][j], lcs_dp[i][j-1])

print(lcs_dp[len(s1)][len(s2)])