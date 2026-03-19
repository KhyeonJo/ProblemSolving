def sum(row, col):
    result = 0
    for i in range(len(row)):
        result += row[i] * col[i]
    return result
    

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
L1 = []
L2 = []
resL = []
for i in range(N):
    l = list(map(int, input().split()))
    L1.append(l)

M, K = map(int, input().split())
for i in range(M):
    l = list(map(int, input().split()))
    L2.append(l)

for i in range(N):
    for j in range(K):
        row = L1[i]
        col = [cl[j] for cl in L2]
        print(sum(row, col), end=' ')
    print()
