import sys
input = sys.stdin.readline

def round(N):
    left = N - int(N)
    if left >= 0.5:
        return int(N)+1
    else:
        return int(N)

N = int(input())
L = []

if N!=0:
    for i in range(N):
        L.append(int(input()))
    
    L.sort()
    
    del_cnt = round(N * 0.15)
    
    result = 0

    for i in range(del_cnt, N-del_cnt):
        result +=L[i]
    print(round(result/(N-del_cnt*2)))
    
else:
    print(N)