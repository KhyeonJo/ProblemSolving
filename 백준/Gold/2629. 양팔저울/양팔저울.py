import sys
input = sys.stdin.readline

pen_num = int(input())
pen_wgt = list(map(int, input().split()))
prl_num = int(input())
prl_wgt = list(map(int, input().split()))
dp = [[0 for i in range(500*j + 1)] for j in range(pen_num+1)]
L = []

def dfs(idx, now): #pendul을 통해 모든 숫자가능 시리즈 생성
    if idx > pen_num: #
        return

    if dp[idx][now] == 1:
        return
    
    dp[idx][now] = 1

    dfs(idx+1, now+pen_wgt[idx-1])
    dfs(idx+1, now)
    dfs(idx+1, abs(now-pen_wgt[idx-1]))

    

dfs(0, 0)

for i in range(prl_num):
    if prl_wgt[i] > 500 * pen_num:
        L.append('N')
    elif dp[pen_num][prl_wgt[i]] == 1:
        L.append('Y')
    else:
        L.append('N')

print(*L)