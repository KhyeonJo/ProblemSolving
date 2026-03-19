N = int(input())
L  = []


for i in range(N):
    num, name = input().split()
    L.append((num, name))


L.sort(key=lambda x: int(x[0]))

for i in range(N):
    print(L[i][0], end=' ')
    print(L[i][1])