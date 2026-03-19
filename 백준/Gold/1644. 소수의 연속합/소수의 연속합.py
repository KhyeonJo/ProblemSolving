import math
import sys
input = sys.stdin.readline

N = int(input())
deci_L = [i for i in range(N+1)]

for i in range(2, N+1):
    if deci_L[i]!=0:
        j = 2
        while i*j <= N:
            deci_L[i*j] = 0
            j +=1

deci_l = []
for deci in deci_L[2:]:
    if deci != 0:
        deci_l.append(deci)

if not deci_l:
    print(0)
    sys.exit()

cnt = 0
start, end = 0, 0
now_sum = deci_l[0]
while end<len(deci_l):
    if now_sum < N:
        end +=1
        if end == len(deci_l):
            break
        now_sum +=deci_l[end]
    elif now_sum > N:
        start +=1
        now_sum -=deci_l[start-1]
    else:
        cnt +=1
        start +=1
        end +=1
        if end == len(deci_l):
            break
        now_sum -=deci_l[start-1]
        now_sum +=deci_l[end]

print(cnt)