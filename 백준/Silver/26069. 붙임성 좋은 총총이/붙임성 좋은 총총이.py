N = int(input())
clt = set()
clt.add("ChongChong")

for i in range(N):
    A, B = input().split()
    if A in clt:
        clt.add(B)
    elif B in clt:
        clt.add(A)

print(len(clt))