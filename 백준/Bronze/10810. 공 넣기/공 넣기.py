N, M = map(int, input().split())
L = [0] * N
for i in range(M):
    start, end, num = map(int, input().split())
    for i in range(start-1, end):
        L[i] = num

print(*L)