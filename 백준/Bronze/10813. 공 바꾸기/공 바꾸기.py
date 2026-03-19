N, M = map(int, input().split())
L = list(map(int, range(1, N+1)))

for i in range(M):
    a, b = map(int, input().split())
    buf = L[a-1]
    L[a-1] = L[b-1]
    L[b-1] = buf

print(*L)