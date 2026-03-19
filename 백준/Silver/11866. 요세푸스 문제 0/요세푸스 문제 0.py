N, K = map(int, input().split())

L = list(range(1,N+1))
i = K-1


print("<", end="")

while 1:
    print(L[i], end="")
    del L[i]
    if L == []:
        break
    print(", ", end="")
    i = (i-1+K) % len(L)
print(">")