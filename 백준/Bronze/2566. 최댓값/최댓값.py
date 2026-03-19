max = 0
ft = 1
sd = 1

for i in range(9):
    L = list(map(int, input().split()))
    for j in range(9):
        if L[j]>=max:
            max = L[j]
            ft = i
            sd = j

print(max)
print(ft+1, sd+1)