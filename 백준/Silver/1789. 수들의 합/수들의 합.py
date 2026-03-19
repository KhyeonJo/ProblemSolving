S = int(input())

tot = 0
i = 0
while tot < S:
    i +=1
    tot +=i

if tot > S:
    i -=1

print(i)