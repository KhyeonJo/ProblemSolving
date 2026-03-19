A, B= map(int, input().split())

L = []
i = 0
while len(L) < B+1:
    i +=1
    for j in range(i):
        L.append(i)

print(sum(L[A-1:B]))