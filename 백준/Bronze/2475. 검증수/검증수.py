L = list(map(int, input().split()))
sum = 0
for i in range(5):
    sum = sum + L[i] * L[i]

print(sum%10)