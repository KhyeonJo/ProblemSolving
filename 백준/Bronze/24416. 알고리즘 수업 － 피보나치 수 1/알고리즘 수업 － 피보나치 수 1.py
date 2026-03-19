N = int(input())

L = [0] * (N+1)

for i in range(1, N+1):
    if i==1 or i==2:
        L[i] = 1
    else:
        L[i] = L[i-1] + L[i-2]



print(L[N], N-2)