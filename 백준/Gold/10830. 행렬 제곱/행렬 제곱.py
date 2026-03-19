def times(N, A, B):
    if B == 1:
        return A
    elif B == 0:
        L = [[0]*N for i in range(N)]
        for i in range(N):
            for j in range(N):
                if i==j:
                    L[i][j] = 1
        return L
    half = times(N, A, B//2)
    if B%2==0:
        return mat_multi(half, half, N)
    else:
        return mat_multi(mat_multi(half, half, N), A, N)

def mat_multi(mat1, mat2, N):
    result = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] +=(mat1[i][k]*mat2[k][j])
            result[i][j] %=1000
    return result

import sys
input = sys.stdin.readline

N, B = map(int, input().split())
A = []
for i in range(N):
    A.append(list(map(int, input().split())))

ans = times(N, A, B)
if B==1:
    for i in range(N):
        for j in range(N):
            print(A[i][j]%1000, end=' ')
        print()
else:
    for i in range(N):
        print(*ans[i])