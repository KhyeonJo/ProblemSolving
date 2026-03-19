N,M = map(int, input().split())

L1 = []
L2 = []

for i in range(N):
    L1.append(list(map(int, input().split())))
    
for i in range(N):
    L2.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        L1[i][j] +=L2[i][j]

for i in range(N):
    print(*L1[i])