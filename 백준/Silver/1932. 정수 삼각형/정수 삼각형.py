import sys
input = sys.stdin.readline

N = int(input())
L = []
for i in range(N):
    L.append(list(map(int, input().split())))

memo = []
for i in range(N):
    memo.append([0]*(i+1))
memo[0][0] = L[0][0]

for i in range(1, N):
    for j in range(i+1):
        if j==0:
            memo[i][j] = memo[i-1][j] + L[i][j]
        elif i==j:
            memo[i][j] = memo[i-1][j-1] + L[i][j]
        else:
            memo[i][j] = max(memo[i-1][j], memo[i-1][j-1]) + L[i][j]
        


#각 자리까지의 최대값 계산
print(max(memo[-1]))