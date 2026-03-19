import sys
N = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))

L.sort()

for i in range(len(L)):
    if i==0:
        continue
    L[i] = L[i] + L[i-1]

print(sum(L))