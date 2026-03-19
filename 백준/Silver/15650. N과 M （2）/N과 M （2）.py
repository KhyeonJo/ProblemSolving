import sys

N, M = map(int, sys.stdin.readline().split())
L = []

def dfs(num):
    if len(L)==M:
        print(*L)
        return
    for i in range(num+1, N+1):
        L.append(i)
        dfs(i)
        L.pop()

dfs(0)