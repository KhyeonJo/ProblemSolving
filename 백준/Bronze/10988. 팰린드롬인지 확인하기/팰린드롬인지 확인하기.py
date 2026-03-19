N = input()
ans = 1
for i in range(len(N)//2):
    if N[i] != N[len(N)-i-1]:
        ans = 0

print(ans)