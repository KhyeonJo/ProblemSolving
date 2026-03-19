import sys

N, M = map(int, sys.stdin.readline().split())
L = []

def dfs():
    if len(L)==M:
        print(*L)
        return
    for i in range(1, N+1):
        L.append(i)
        dfs()
        L.pop()

dfs()