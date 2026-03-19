N = int(input())
sum =0
L = list(map(int, input().split()))
V = int(input())

for i in range(N):
    if V == L[i]:
        sum =sum+1

print(sum)