from itertools import combinations
import sys
input = sys.stdin.readline


N, C = map(int, input().split())
items = list(map(int, input().split()))
A, B = items[:N//2], items[N//2:]


a = []
b = []
for i in range(len(A)+1):
    comb = combinations(A, i)

    for j in comb:
        a.append(sum(j))

for i in range(len(B)+1):
    comb = combinations(B, i)

    for j in comb:
        b.append(sum(j))
        
cnt = 0
a.sort()

for b_sum in b:
    if b_sum > C:
        continue
    start, end = 0, len(a)-1

    while start<=end:
        mid = (start+end)//2

        if b_sum + a[mid] <= C:
            start = mid + 1
        else:
            end = mid - 1

    cnt += end+1

print(cnt)