import sys
T = int(sys.stdin.readline().strip())

for i in range(T):
    N = int(sys.stdin.readline().strip())
    L = [(0,0)]*(N+1)
    for j in range(N+1):
        if j==1:
            L[j] = (0,1)
        elif j==0:
            L[j] = (1,0)
        else:
            L[j] = (L[j-1][0] + L[j-2][0], L[j-1][1] + L[j-2][1])
            
    print(*L[N])