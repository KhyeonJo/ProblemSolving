import sys

N, M = map(int, sys.stdin.readline().split())

L = []

for i in range(1, N+1):
    L.append(i)


for a in range(M):
    i, j = map(int, sys.stdin.readline().split())
    A = L[0:i-1]
    B = list(reversed(L[i-1:j]))
    C = L[j:N]
    L = A+B+C


print(*L)