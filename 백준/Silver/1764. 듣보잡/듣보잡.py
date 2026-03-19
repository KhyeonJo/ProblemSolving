import sys

N, M = map(int, sys.stdin.readline().split())
Nset = set()
Mset = set()

for i in range(N):
    Nset.add(sys.stdin.readline().strip())

for i in range(M):
    Mset.add(sys.stdin.readline().strip())

ans = list(Nset & Mset)

print(len(ans))

for i in sorted(ans):
    print(i)