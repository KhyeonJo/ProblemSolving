import sys
N =int(sys.stdin.readline())
L = [0] * N
for i in range(N):
    L[i] = int(sys.stdin.readline())

newL = sorted(L)

for i in range(N):
    print(newL[i])