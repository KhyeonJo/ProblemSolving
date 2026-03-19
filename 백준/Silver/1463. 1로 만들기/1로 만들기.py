import sys
N = int(sys.stdin.readline())

L = [0] * (N*3+100)
L[0], L[1]= 0, 0

for i in range(2,N+1):
    L[i] = L[i-1] + 1
    if i%3==0:
        L[i] = min(L[i], L[i//3]+1)
    if i%2==0:
        L[i] = min(L[i], L[i//2]+1)

print(L[N])