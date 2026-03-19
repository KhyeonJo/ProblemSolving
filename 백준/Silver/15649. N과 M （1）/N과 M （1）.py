import sys

N, M = map(int, sys.stdin.readline().split())
L = []


def dfs():
    if len(L)==M:
        print(*L)
        return
    for i in range(N):
        if i+1 not in L:
            L.append(i+1)
            dfs()
            L.pop()
        
dfs()