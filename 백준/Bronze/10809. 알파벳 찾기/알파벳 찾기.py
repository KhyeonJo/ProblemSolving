N = list(map(ord, input()))

L = [-1] * 26

for i in sorted(range(len(N)), reverse=True):
    L[N[i]-97] = i

print(*L)