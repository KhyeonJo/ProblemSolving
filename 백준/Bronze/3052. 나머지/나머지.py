L = [50] * 10
tot = 0

for i in range(10):
    N = int(input())%42
    for j in range(10):
        if L[j] == N:
            tot = tot - 1
            break
    tot = tot + 1
    L[i] = N
print(tot)