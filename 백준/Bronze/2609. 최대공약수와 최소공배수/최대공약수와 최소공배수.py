A, B= map(int, input().split())

for i in range(1, max(A,B)+1):
    if A%i ==0:
        if B%i == 0:
            GCD = i

LCM = 0
times = 0
while LCM == 0:
    times = times + 1
    if max(A,B)*times % A == 0:
        if max(A,B)*times % B == 0:
            LCM = max(A,B)*times

print(GCD)
print(LCM)