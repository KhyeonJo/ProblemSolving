import sys
input = sys.stdin.readline


N = int(input())
L = []
for _ in range(N):
    l = list(input())
    L.append(l)
    
def check_len():
    mx_cnt = 1
    for i in range(N):
        cnt = 1
        for j in range(N-1):
            if L[i][j] == L[i][j+1]:
                cnt +=1
            else:
                cnt = 1
            if cnt > mx_cnt:
                mx_cnt = cnt

    for i in range(N):
        cnt = 1
        for j in range(N-1):
            if L[j][i] == L[j+1][i]:
                cnt +=1
            else:
                cnt = 1
            if cnt > mx_cnt:
                mx_cnt = cnt
    return mx_cnt

ans = 1
for i in range(N):
    for j in range(N-1):
        L[i][j], L[i][j+1] = L[i][j+1], L[i][j]
        ans = max(ans, check_len())
        L[i][j], L[i][j+1] = L[i][j+1], L[i][j]

        L[j][i], L[j+1][i] = L[j+1][i], L[j][i]
        ans = max(ans, check_len())
        L[j][i], L[j+1][i] = L[j+1][i], L[j][i]

print(ans)