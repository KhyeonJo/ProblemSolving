N, M = map(int, input().split())
L = list(map(int, input().split()))
max = 0

for i in range(len(L)-2):
    for j in range(i+1, len(L)-1):
        for k in range(j+1, len(L)):
            if L[i] + L[j] + L[k] > max and L[i] + L[j] + L[k] <= M:
                max = L[i] + L[j] + L[k]

print(max)